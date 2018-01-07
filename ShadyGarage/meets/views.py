from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import ListView
from . import models
=======
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from . import models
from . import forms

>>>>>>> a8c4cfe7bdf32f17e62d97c794696e0679bb462b
# Create your views here.

class MeetsListView(ListView):
    template_name = 'meets/meets_list.html'
    model = models.Meet
<<<<<<< HEAD
=======

class CreateMeetView(CreateView):
    template_name = 'meets/meets_form.html'
    form_class = forms.CreateMeetForm
    success_url = reverse_lazy('home')
>>>>>>> a8c4cfe7bdf32f17e62d97c794696e0679bb462b
