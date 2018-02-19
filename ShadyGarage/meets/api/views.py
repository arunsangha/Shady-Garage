from rest_framework import generics
from .serializers import MeetsModelSerializer
from posts.api.pagination import StandardResultsPagination
from meets.models import Meet
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

class MeetsListAPIView(generics.ListAPIView):
    serializer_class = MeetsModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Meet.objects.all()
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(user_fk__username__icontains=query) |
                Q(meet_name__icontains=query) |
                Q(date__icontains=query) |
                Q(time__icontains=query) |
                Q(description__icontains=query) |
                Q(users_joining__username__icontains=query)
            )

        return qs

class JoinToggleAPIView(APIView):
    def get(self, request, pk, format=None):
        meet_qs = Meet.objects.filter(pk=pk)
        is_joining = Meet.objects.join_toggle(request.user, meet_qs.first())
        return Response({'joining':is_joining})
