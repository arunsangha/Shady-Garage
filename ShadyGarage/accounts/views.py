from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from . import forms
from django.views.generic import CreateView, UpdateView, TemplateView

def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data = request.POST)

        if user_form.is_valid():
            new_user = user_form.save()
            new_user = authenticate(username = user_form.cleaned_data['username'], password = user_form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect("accounts:signup_del2")

    else:
        user_form = forms.UserForm()
    return render(request, "accounts/signup.html", {'user_form': user_form})

class ProfileInfo(CreateView, LoginRequiredMixin):
    form_class = forms.ProfileForm
    template_name = "accounts/profile_info.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProfilePage(TemplateView):
    template_name = "accounts/profilepage.html"


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user.profile)

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
    return render(request, 'accounts/activity.html', {'user':user})
