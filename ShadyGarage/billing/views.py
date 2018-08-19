from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import BillingProfile, Card

#Gets token from ajax and creates a new card object for user. Then sets the card id in session.
def payment_method_createview(request):
    if request.method == 'POST' and request.is_ajax():
        billing_profile, created = BillingProfile.objects.new_or_get(request=request)
        if not billing_profile:
            return HttpResponse({'message':'Cant find this user!'},status=401)

        token = request.POST.get('token')
        if token is not None:
            new_card = Card.objects.add_new(billing_profile=billing_profile, token=token)
            # TODO: add token to session
        return JsonResponse({'message':'Done'})

    return HttpResponse({'error':'Not correct request'}, status=401)
