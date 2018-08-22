from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from . import forms
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from posts.models import Notification
from orders.models import Order
from billing.models import BillingProfile
def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)

        if user_form.is_valid():
            new_user = user_form.save()
            new_user = authenticate(username = user_form.cleaned_data['username'], password = user_form.cleaned_data['password1'],)
            login(request, new_user)
            id = new_user.id
            return HttpResponseRedirect(reverse("accounts:signup_del2", kwargs={'pk':request.user.id}))


    else:
        user_form = forms.UserForm()
    return render(request, "accounts/signup.html", {'user_form': user_form})

class ProfileInfo(UpdateView, LoginRequiredMixin):
    queryset = models.Profile.objects.all()
    form_class = forms.ProfileForm
    template_name = "accounts/profile_info.html"

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(ProfileInfo, self).form_valid(form)
        else:
            return HttpResponseRedirect(reverse("accounts:signup"))

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("meets:meets_list")

class ProfilePage(TemplateView):
    template_name = "accounts/profilepage.html"

# TODO: Opplasting av feil fil i edit profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, request.FILES or None, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile_page')

    else:
        form = forms.EditProfileForm(instance=request.user.profile)
        return render(request, 'accounts/edit_profile.html', {'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile_page')

        else:
            return redirect('accounts:change_password')

    else:
        form = PasswordChangeForm(user = request.user)
        return render(request, 'accounts/change_password.html', {'form':form})

def view_profiles(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, 'accounts/profilepage.html', {'user':user})

def ProfileActivity(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    notifications = Notification.objects.filter(owner=user)
    return render(request, 'accounts/activity.html', {'user':user, 'notifications':notifications})

class MyOrders(ListView):
    template_name = "accounts/my_orders.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MyOrders, self).get_context_data(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        billing_profile, created = BillingProfile.objects.new_or_get(self.request)
        qs = Order.objects.filter(billing_profile=billing_profile, status='paid')
        return qs
