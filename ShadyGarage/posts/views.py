from django.shortcuts import render, HttpResponseRedirect
from . import models
from . import forms
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from django.core.urlresolvers import reverse_lazy, reverse

# Create your views here.

class PostList(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'

class PostDetail(DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'

class PostForm(CreateView):
    form_class = forms.PostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        post_form = form.save(commit = False)
        post_form.user_fk = self.request.user
        post_form.save()

        return HttpResponseRedirect(reverse("posts:posts_feed"))

class PostLikeToggleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get['slug']
        obj = get_object_or_404(models.Post, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.post_like.all():
                obj.post_like.remove(user)
            else:
                obj.post_like.add(user)

        return url_
