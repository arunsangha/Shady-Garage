from rest_framework import generics
from .serializers import MeetsModelSerializer, MeetCommentSerializer
from posts.api.pagination import StandardResultsPagination, ProfilePostResultsPagination
from meets.models import Meet, Meet_Comment
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import CommentResultsPagination
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import authentication

from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class SampleApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)    

    def get(self, request, format=None):
        print(request.user)
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

@method_decorator(csrf_exempt, name='dispatch')
class JoinMeetAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,) 
    def get(self, request, format=None):
        meet_qs = Meet.objects.filter(slug=request.data['pk'])
        is_joining = Meet.objects.join_toggle(request.user, meet_qs.first())
        return Response({'joining':is_joining})



class MeetsListAPIView(generics.ListAPIView):
    serializer_class = MeetsModelSerializer
    pagination_class = ProfilePostResultsPagination

    def get_queryset(self, *args, **kwargs):
        today = datetime.now().date()
        qs = Meet.objects.filter(Q(date__gte=today))
        query = self.request.GET.get('q',None)
        if query is not None:
            print("Query is not none")
            qs = qs.filter(
                Q(user_fk__username__icontains=query) |
                Q(meet_name__icontains=query) |
                Q(date__icontains=query) |
                Q(time__icontains=query) |
                Q(description__icontains=query) |
                Q(adress__icontains=query) |
                Q(city__icontains=query)
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
