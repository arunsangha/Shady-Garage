from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class MeetsListView(ListView):
    template_name = 'meets/meets_list.html'
    model = models.Meet
