from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse_lazy
from . import models
from . import forms

# Create your views here.

class MeetsListView(ListView):
    template_name = 'meets/meets_list.html'
    model = models.Meet

class CreateMeetView(CreateView, LoginRequiredMixin):
    template_name = 'meets/meets_form.html'
    form_class = forms.CreateMeetForm

class DetailMeetView(DetailView):
    template_name = 'meets/meets_detail.html'
    model = models.Meet
