from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from . import models
from . import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
# Create your views here.

class MeetsListView(ListView):
    template_name = 'meets/meets_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MeetsListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = models.Meet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(date__icontains=query) |
                Q(meet_name__icontains=query) |
                Q(description__icontains=query) |
                Q(time__icontains=query)
            )
        return qs

class CreateMeetView(LoginRequiredMixin, CreateView):
    template_name = 'meets/meets_form.html'
    form_class = forms.CreateMeetForm
    success_url = reverse_lazy('meets:meets_list')

class DetailMeetView(LoginRequiredMixin, DetailView):
    template_name = 'meets/meets_detail.html'
    model = models.Meet

class MeetJoinToggleView(RedirectView):
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

class CommentView(LoginRequiredMixin, CreateView):
    form_class = forms.CommentForm
    template_name = "meets/meets_comment.html"

    def form_valid(self, form):
        meet_comment = form.save(commit = False)
        slug = self.kwargs.get('slug')
        meet_comment.meet_fk = get_object_or_404(models.Meet, slug=slug)
        meet_comment.user = self.request.user
        meet_comment.save()

        return HttpResponseRedirect(reverse("meets:single", kwargs={'slug':slug}))
