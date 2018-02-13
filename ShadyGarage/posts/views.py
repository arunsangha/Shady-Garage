from django.shortcuts import render, HttpResponseRedirect
from . import models
from . import forms
from django.views.generic import ListView, CreateView, DetailView, RedirectView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
# Create your views here.

class PostList(LoginRequiredMixin, ListView):
    template_name = 'posts/post_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = models.Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(user_fk__username__icontains=query) |
                Q(post_title__icontains=query) |
                Q(post_description__icontains=query)
            )
        return qs

class PostDetail(LoginRequiredMixin, DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'

class PostForm(LoginRequiredMixin, CreateView):
    form_class = forms.PostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        post_form = form.save(commit = False)
        post_form.user_fk = self.request.user
        post_form.save()

        return HttpResponseRedirect(reverse("posts:posts_feed"))



class PostDeleteView(DeleteView):
    model = models.Post
    template_name = "posts/delete_confirm.html"
    success_url = reverse_lazy("posts:posts_feed")
