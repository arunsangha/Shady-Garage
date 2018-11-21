from django.shortcuts import render, redirect
from .models import Cart
from products.models import ProductItem, ProductSize, Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from billing.models import BillingProfile, Card
from addresses.forms import AddressForm
from addresses.models import Address
from orders.models import Order
from django.views.generic import TemplateView
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def cart_home(request):
    cart_obj, created = Cart.objects.get_or_create(request)
    return render(request, "carts/cart_home.html", {'cart':cart_obj})

def cart_add(request):
    cart_obj, created = Cart.objects.get_or_create(request)
    pk = request.POST.get('pk')
    size = request.POST.get('size')
    quantity = request.POST.get('quantity')

    try:
        product_item = ProductSize.objects.get(product_fk=pk, size=size)

    except ProductSize.DoesNotExist:
        if request.is_ajax():
            return JsonResponse({'success':False, 'message':'Product size dosent exist..'})
        redirect("carts:cart-home")

    product_, created = ProductItem.objects.get_or_create(product_size_fk=product_item)

    if product_ in cart_obj.products.all():
        added = False
        cart_obj.products.remove(product_)
    else:
        added = True
        cart_obj.products.add(product_)

    cart_products_count = 0
    for p in cart_obj.products.all():
        cart_products_count += p.quantity
    request.session['cart_products_count'] = cart_products_count

    if request.is_ajax():
        data = {
            'added':added,
            'removed': not added,
            'cartItemCount': cart_obj.products.count(),
            'subTotal': cart_obj.sub_total,
            'total': cart_obj.total,
            'shipping': cart_obj.shipping,
            'cartProductCount':cart_products_count,
        }

        return JsonResponse(data)

    return redirect("carts:cart-home")


def cart_update_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        cart_obj, created = Cart.objects.new_or_get(request)
        response = {"success":"False"}
        try:
            product_cart_obj = get_object_or_404(ProductItem, pk=product_cart)
        except ProductItem.DoesNotExist:
            return JsonResponse(response)

        quantity = request.POST.get('quantity')
        if quantity:
            product_cart_obj.quantity = quantity
            product_cart_obj.save()
            updated = cart_obj.update_prices()
            price = cart_obj.price
            response = {
                "success":"True",
                "price":price

                }
        return JsonResponse(response)
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
        addresses = Address.objects.all().filter(user=billing_profile).exclude(address_type='billing')
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

                    subject, from_email, to = 'Bekreftelse på ordre!', 'shadygarage.no@gmail.com', billing_profile.email
                    adr = order_obj.shipping_address.address_line_1 + ", " + order_obj.shipping_address.post_code + " " + order_obj.shipping_address.city
                    vars = {
                        'username': request.user.username,
                        'order_id':order_obj.order_id,
                        'shipping_address': adr,
                    }
                    html_content = render_to_string('email_order_confirm.html', vars)
                    text_content = strip_tags(html_content)
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()

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
