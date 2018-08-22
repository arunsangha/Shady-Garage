from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import AddressForm
from billing.models import BillingProfile
from django.http import JsonResponse
# Create your views here.

def create_address(request):
    form = AddressForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        billing_obj, created = BillingProfile.objects.new_or_get(request=request)

        success = False
        isShippingAddress = True
        if billing_obj is not None:
            instance.user = billing_obj

            #Send a hidden input white name "adress_type" that says something about the adress_type
            instance.address_type = request.POST.get('address_type', 'shipping')
            instance.save()
            if instance.address_type == 'shipping':
                request.session['shipping_address_id'] = instance.id
            else:
                request.session['billing_address_id'] = instance.id
                isShippingAddress = False
            success = True

        if request.is_ajax():
            data = {
                'success':success,
                'isShippingAddress':isShippingAddress,
            }

            return JsonResponse(data)

        return redirect("carts:cart-checkout")

def reuse_address(request):
    if request.method == "POST":
        
        pk = request.POST.get('pk', 0)
        type = request.POST.get('type', 'shipping')

        if type == "shipping":
            if 'shipping_address_id' in request.session:
                del request.session['shipping_address_id']
            request.session['shipping_address_id'] = pk
        else:
            print("HALLO")
            if 'billing_address_id' in request.session:
                del request.session['billing_address_id']
            request.session['billing_address_id'] = pk

    if request.is_ajax():
        pk = request.POST.get('pk', 0)
        type = request.POST.get('type', 'shipping')
        success = False

        if type == "shipping":
            if 'shipping_address_id' in request.session:
                del request.session['shipping_address_id']
            request.session['shipping_address_id'] = pk
            success = True
        else:
            if 'billing_address_id' in request.session:
                print("EXISTS")
                del request.session['billing_address_id']
            request.session['billing_address_id'] = pk
            success = True
        return JsonResponse({"success":success})

    return redirect("carts:cart-checkout")
