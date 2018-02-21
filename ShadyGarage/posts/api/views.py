from rest_framework import generics, permissions
from posts.models import Post
from .serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(PostListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

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

class LikeToggleAPIView(APIView):
    def get(self, request, pk, format=None):
        post_qs = Post.objects.filter(pk=pk)
        is_liked = Post.objects.like_toggle(request.user, post_qs.first())
        return Response({'liked':is_liked})

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user_fk=self.request.user)
