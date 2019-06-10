from django.conf.urls import url
from .views import (MeetsListAPIView, 
    JoinToggleAPIView, MeetsCommentListAPIView, 
    JoinMeetAPIView,
    IsJoiningAPIView,
    CreateMeetAPIView)
urlpatterns = [
    url(r'^$', MeetsListAPIView.as_view(), name="meets-list-api-view"),
    url(r'^(?P<pk>\d+)/join/$', JoinToggleAPIView.as_view(), name="api-join-view"),
    url(r'^(?P<pk>\d+)/comments/$', MeetsCommentListAPIView.as_view(), name="meets-comment-list-api"),
    url(r'^joinmeet/$', JoinMeetAPIView.as_view(), name="api-join-meet-view"),
    url(r'^joining/$', IsJoiningAPIView.as_view(), name="api-is-joining"),
    url(r'^createmeet/$', CreateMeetAPIView.as_view(), name="api-create-meet")
]
