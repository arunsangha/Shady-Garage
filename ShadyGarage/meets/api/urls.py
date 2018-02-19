from django.conf.urls import url
from .views import MeetsListAPIView, JoinToggleAPIView
urlpatterns = [
    url(r'^$', MeetsListAPIView.as_view(), name="meets-list-api-view"),
    url(r'^(?P<pk>\d+)/join/$', JoinToggleAPIView.as_view(), name="api-join-view"),
]
