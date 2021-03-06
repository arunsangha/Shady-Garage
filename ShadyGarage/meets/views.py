from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, CreateView,
        DetailView, RedirectView, DeleteView, UpdateView, TemplateView)
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

    def form_valid(self, form):
        meet_form = form.save(commit = False)
        meet_form.user_fk = self.request.user
        meet_form.save(commit = True)
        slug = meet_form.slug
        return HttpResponseRedirect(reverse("meets:single", kwargs={'slug':slug}))

class UpdateMeetView(LoginRequiredMixin, UpdateView):
    queryset = models.Meet.objects.all()
    template_name = 'meets/meet_update.html'
    form_class = forms.CreateMeetForm

    def form_valid(self, form):
        if form.instance.user_fk == self.request.user:
            return super(UpdateMeetView, self).form_valid(form)
        else:
            slug = self.kwargs['slug']
            return HttpResponseRedirect(reverse("meets:meet_update_fail", kwargs={'slug':slug}))

    def get_success_url(self):
        slug_field = self.kwargs.get('slug')
        return reverse("meets:meets_list")

class MeetUpdateFail(TemplateView):
    template_name = 'update_invalid.html'

class DetailMeetView(DetailView):
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

class MeetDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Meet
    template_name = "meets/delete_confirm.html"
    success_url = reverse_lazy("meets:meets_list")

class MeetCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Meet_Comment
    template_name = "meets/comment_delete.html"

    def get_success_url(self):
        slug = self.kwargs.get('slug')
        return reverse_lazy('meets:single', kwargs={'slug':slug})

class MeetsMarkersList(TemplateView):
    template_name = 'meets/meets_markers_list.html'


class AdminMessageCreate(CreateView):
    template_name = 'meets/adminmessage_form.html'
    form_class = forms.AdminMessageForm

    def form_valid(self, form):
        admin_message = form.save(commit=False)
        meet_slug = self.kwargs.get('slug')
        meet = models.Meet.objects.get(slug=meet_slug)
        request_user = self.request.user
        if request_user == meet.user_fk:
            admin_message.owner = request_user
            admin_message.meet = meet
            admin_message.save()
            return HttpResponseRedirect(reverse("meets:single", kwargs={'slug':meet_slug}))

        return HttpResponseRedirect(reverse("meets:single", kwargs={'slug':meet_slug}))
