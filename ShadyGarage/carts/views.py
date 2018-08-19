from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from billing.models import BillingProfile
from addresses.forms import AddressForm
from addresses.models import Address
from orders.models import Order
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


    request.session['cart_total'] = cart_obj.products.count()

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

    address_form = AddressForm()
    billing_profile, created = BillingProfile.objects.new_or_get(request)

    if billing_profile is not None:

        #order_obj, created = Order.objects.new_or_get(billing_profile=billing_profile, cart=cart_obj)

        # TODO: Legge til order & card i session for siste checkout del.

        shipping_address_id = request.session.get("shipping_address_id", None)
        billing_adress_id = request.session.get("billing_address_id", None)

        shipping_address = None
        hasShippingAddress = False
        if shipping_address_id:
            shipping_address = Address.objects.get(id=shipping_address_id)
            hasShippingAddress = True

        billing_address = None
        hasBillingAddress = False
        billing_address_id = request.session.get("billing_address_id", None)
        if billing_adress_id:
            billing_address = Address.objects.get(id=billing_address_id)
            hasBillingAddress = True

    if created:
        print("FUCK OFF")

    context = {
        'billing_profile':billing_profile,
        'address_form':address_form,
        'hasShippingAddress':hasShippingAddress,
        'shipping_address':shipping_address,
        'hasBillingAddress':hasBillingAddress,
        'billingAddress':billing_address,
    }
    return render(request, "carts/cart-checkout.html", context)
