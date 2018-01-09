from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.views.generic import CreateView, TemplateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserForm
    template_name="accounts/signup.html"
    success_url = reverse_lazy("login")

class ProfileInfo(CreateView):
    form_class = forms.ProfileForm
    template_name = "accounts/profile_info.html"
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
