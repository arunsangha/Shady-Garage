from rest_framework.generics import ListAPIView
from blogs.models import Blog
from .serializers import BlogListSerializer
from django.db.models import Q
from posts.api.pagination import StandardResultsPagination

class BlogListAPIView(ListAPIView):
    serializer_class = BlogListSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(BlogListAPIView,self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request

    def get_queryset(self):
        qs = Blog.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query),
                Q(car__make__icontains=query),
                Q(car__model__icontains=query),
                Q(car__hp__icontains=query),
                Q(car__engine__icontains=query),
            )
        return qs
