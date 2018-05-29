from rest_framework import generics
from .serializers import MeetsModelSerializer, MeetCommentSerializer
from posts.api.pagination import StandardResultsPagination, ProfilePostResultsPagination
from meets.models import Meet, Meet_Comment
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import CommentResultsPagination
import datetime

class MeetsListAPIView(generics.ListAPIView):
    serializer_class = MeetsModelSerializer
    pagination_class = ProfilePostResultsPagination

    def get_queryset(self, *args, **kwargs):
        date_now = datetime.datetime.now()
        qs = Meet.objects.all()
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(user_fk__username__icontains=query) |
                Q(meet_name__icontains=query) |
                Q(date__icontains=query) |
                Q(time__icontains=query) |
                Q(description__icontains=query) |
                Q(users_joining__username__icontains=query) |
                Q(location__icontains=query)
            )

        return qs

class JoinToggleAPIView(APIView):
    def get(self, request, pk, format=None):
        meet_qs = Meet.objects.filter(pk=pk)
        is_joining = Meet.objects.join_toggle(request.user, meet_qs.first())
        return Response({'joining':is_joining})

class MeetsCommentListAPIView(generics.ListAPIView):
    serializer_class = MeetCommentSerializer
    pagination_class = CommentResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(MeetsCommentListAPIView, self).get_serializer_context(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Meet_Comment.objects.filter(meet_fk=self.kwargs.get('pk'))
        return qs
