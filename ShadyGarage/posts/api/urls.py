from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(),name="post-api"),
    url(r'^(?P<pk>\d+)/like/$', views.LikeToggleAPIView.as_view(), name="api-like-view"),
    url(r'^shady/create/$', views.PostCreateAPIView.as_view(), name="api-create-view"),
]
