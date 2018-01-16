from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, RedirectView
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

class MeetJoinToogleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(models.Meet, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.users_joining.all():
                obj.users_joining.remove(user)
            else:
                obj.users_joining.add(user)
        return url_
