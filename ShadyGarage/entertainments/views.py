from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, TemplateView, ListView
from . import forms
from . import models
from django.core.urlresolvers import reverse
# Create your views here.

class EntertainmentCreate(CreateView):
    template_name = "entertainments/create.html"
    form_class = forms.Entertainment

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user_fk = self.request.user
        form.save()
        return HttpResponseRedirect(reverse('entertainments:list'))



class EntertainmentList(ListView):
    template_name = "entertainments/list.html"

    def get_queryset(self, *args, **kwargs):
        qs = models.Entertainment.objects.all()
        return qs
