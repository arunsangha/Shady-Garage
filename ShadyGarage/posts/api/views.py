from rest_framework import generics
from posts.models import Post
from .serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(user_fk__username__icontains=query) |
                Q(post_title__icontains=query) |
                Q(post_description__icontains=query) |
                Q(post_created__icontains=query)
            )
        return qs
