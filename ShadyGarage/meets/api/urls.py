from django.conf.urls import url
from .views import MeetsListAPIView, JoinToggleAPIView, MeetsCommentListAPIView, SampleApi
urlpatterns = [
    url(r'^$', MeetsListAPIView.as_view(), name="meets-list-api-view"),
    url(r'^(?P<pk>\d+)/join/$', JoinToggleAPIView.as_view(), name="api-join-view"),
    url(r'^(?P<pk>\d+)/comments/$', MeetsCommentListAPIView.as_view(), name="meets-comment-list-api"),
    url(r'^sampleapi/', SampleApi.as_view(), name="meets-detail-api"),
]
