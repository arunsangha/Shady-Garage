from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from . import models
from . import forms
from django.views.generic import (ListView, CreateView, DetailView,
                RedirectView, DeleteView, UpdateView, TemplateView)
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

class PostCommentCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.PostCommentForm
    template_name = "posts/post_comment.html"


    def form_valid(self, form):
        post_comment = form.save(commit = False)
        slug = self.kwargs.get('slug')
        post_comment.post_fk = get_object_or_404(models.Post, slug=slug)
        post_comment.user_fk = self.request.user
        post_comment.save()

        return HttpResponseRedirect(reverse("posts:post_detail", kwargs={'slug':slug}))

class PostCommentDeleteView(DeleteView):
    model = models.PostComment
    template_name = "posts/comment_delete.html"

    def get_success_url(self):
        slug_field = self.kwargs.get('slug')
        return reverse_lazy("posts:post_detail", kwargs={'slug':slug_field})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    queryset = models.Post.objects.all()
    form_class = forms.PostForm
    template_name = "posts/post_update.html"

    def form_valid(self, form):
        if form.instance.user_fk == self.request.user:
            return super(PostUpdateView, self).form_valid(form)
        else:
            slug = self.kwargs['slug']
            return HttpResponseRedirect(reverse("posts:post_update_fail", kwargs={'slug':slug}))

    def get_success_url(self):
        slug_field = self.kwargs.get('slug')
        return reverse_lazy("posts:post_detail", kwargs={'slug':slug_field})

class PostUpdateFail(TemplateView):
    template_name = "update_invalid.html"
