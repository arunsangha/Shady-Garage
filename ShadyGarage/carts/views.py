from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from billing.models import BillingProfile
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
    billing_profile, created = BillingProfile.objects.new_or_get(request)

    if created:
        print("FUCK OFF")

    return render(request, "carts/cart-checkout.html", {'billing_profile':billing_profile})
