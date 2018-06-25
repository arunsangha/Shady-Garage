from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import EntertainmentSerializer
from .pagination import EntertainmentPagination
from entertainments.models import Entertainment
from rest_framework.response import Response

class EntertainmentList(generics.ListAPIView):
    serializer_class = EntertainmentSerializer
    pagination_class = EntertainmentPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(EntertainmentList, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self):
        qs = Entertainment.objects.all()
        return qs

class EntertainmentLikeToggle(APIView):
    def get(self, request, pk, format=None):
        ent_obj = Entertainment.objects.filter(pk=pk)
        is_liked = Entertainment.objects.like_toogle(request.user, ent_obj.first())
        return Response({'liked':is_liked})
