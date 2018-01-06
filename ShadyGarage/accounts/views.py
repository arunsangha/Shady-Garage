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
    success_url = "merinfo"

class MoreInfo(CreateView, ):
    form_class = forms.ProfileForm
    template_name = "accounts/moreinfo.html"
    success_url = "login"
