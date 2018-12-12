from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView, ListView
# Create your views here.

class BlogDetail(DetailView):
    template_name = "blogs/blogs_detail.html"
    model = Blog

class BlogList(ListView):
    template_name = "blogs/blogs_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Blog.objects.all()
        return qs
 
