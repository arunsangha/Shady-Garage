from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BlogDetail(TemplateView):
    template_name = "blogs/blogs_detail.html"

class BlogList(TemplateView):
    template_name = "blogs/blogs_list.html"
