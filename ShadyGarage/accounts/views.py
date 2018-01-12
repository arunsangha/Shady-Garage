from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms
from django.views.generic import CreateView, UpdateView, TemplateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserForm
    template_name="accounts/signup.html"
    success_url = reverse_lazy("login")

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
