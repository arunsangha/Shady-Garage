from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from billing.models import BillingProfile, Card
from addresses.forms import AddressForm
from addresses.models import Address
from orders.models import Order
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def cart_home(request):
    cart_obj, created = Cart.objects.get_or_create(request)
    return render(request, "carts/cart_home.html", {'cart':cart_obj})

def cart_add(request, pk):
    cart_obj, created = Cart.objects.get_or_create(request)

    try:
        product = Product.objects.get(id=pk)

    except Product.DoesNotExist:
        # TODO: Adde json response her med error?
        redirect("carts:cart-home")

    if product in cart_obj.products.all():
        added = False
        cart_obj.products.remove(product)
    else:
        added = True
        cart_obj.products.add(product)


    request.session['cart_products_count'] = cart_obj.products.count()

    if request.is_ajax():
        data = {
            'added':added,
            'removed': not added,
            'cartItemCount': cart_obj.products.count()
        }

        return JsonResponse(data)

    return redirect("carts:cart-home")


@login_required
def cart_checkout(request):
    order_obj = None
    cart_obj, created = Cart.objects.get_or_create(request)

    addresses = None
    hasAddress = False
    address_form = AddressForm()
    billing_profile, created = BillingProfile.objects.new_or_get(request)

    if billing_profile is not None:
        addresses = Address.objects.all().filter(user=billing_profile)
        if addresses.count() >= 1:
            hasAddress = True
        order_obj, created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)
        request.session['order_id'] = order_obj.id

        shipping_address_id = request.session.get("shipping_address_id", None)
        billing_adress_id = request.session.get("billing_address_id", None)


    if created:
        print("FUCK OFF")

    context = {
        'billing_profile':billing_profile,
        'address_form':address_form,
        'addresses':addresses,
        'hasBillingAddress':True,
        'hasAddress':hasAddress,
    }
    return render(request, "carts/cart-checkout.html", context)

@login_required
def cart_confirm(request):
    billing_profile, created = BillingProfile.objects.new_or_get(request)
    if created:
        return redirect("carts:cart-checkout")

    billing_address_id = request.session.get('billing_address_id')
    shipping_address_id = request.session.get('shipping_address_id')
    card_id = request.session.get('card_id')
    order_id = request.session.get('order_id')
    billing_address = None
    shipping_address = None
    products = None
    card_obj = None
    order_obj = Order.objects.filter(id=order_id)
    error_msg = ""
    if order_obj:
        order_obj = order_obj.first()
        products = order_obj.cart.products.all()
        for x in products:
            if not x.take_one():
                error_msg = "Error! Produktet {product} er tomt! :(".format(product=x.name)
                return render(request, "carts/cart-confirm.html", {'error_msg':error_msg})

        billing_address = Address.objects.get(id=billing_address_id)
        shipping_address = Address.objects.get(id=shipping_address_id)
        card_obj = Card.objects.get(id=card_id)
        if billing_address and shipping_address and card_obj:
            #First because this are querysets
            billing_address = billing_address
            shipping_address = shipping_address
            card_obj = card_obj

            order_obj.shipping_address = shipping_address
            order_obj.billing_address = billing_address

            order_obj.save()

            if request.method == "POST":
                if order_obj.check_done():
                    billing_profile.charge(order_obj=order_obj, card=card_obj)
                    cart_obj = order_obj.cart
                    cart_obj.set_inactive()
                    del request.session['cart_id']
                    del request.session['card_id']
                    del request.session['order_id']

                    order_id = order_obj.order_id
                    order_obj.set_paid()

                    return redirect("carts:cart-success")

    context = {
        'billing_address': billing_address,
        'shipping_address':shipping_address,
        'products':products,
        'card':card_obj,
        'order':order_obj,
    }

    return render(request, "carts/cart-confirm.html", context)

class CartSuccess(TemplateView):
    template_name = "carts/cart-success.html"
