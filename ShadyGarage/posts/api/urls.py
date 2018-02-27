from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(),name="post-api"),
    url(r'^like/(?P<pk>\d+)/$', views.LikeToggleAPIView.as_view(), name="api-like-view"),
    url(r'^create_post/$', views.PostCreateAPIView.as_view(), name="api-create-view"),
    url(r'^create_comment/(?P<slug>[-\w]+)/$', views.PostCommentCreateAPIView.as_view(), name="api-comment-create-view"),
]
