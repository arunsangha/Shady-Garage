from django.conf.urls import url
from . import views

app_name ="posts_api"
urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(),name="post-api"),
    url(r'^like/(?P<pk>\d+)/$', views.LikeToggleAPIView.as_view(), name="api-like-view"),
    url(r'^create_post/$', views.PostCreateAPIView.as_view(), name="api-create-view"),
    url(r'^create_comment/(?P<slug>[-\w]+)/$', views.PostCommentCreateAPIView.as_view(), name="api-comment-create-view"),
    url(r'^create_comment_reply/id/(?P<pk>\d+)/$', views.PostCommentReplyCreateAPIView.as_view(), name="api-comment-reply-create-view"),
    url(r'^accounts/myprofile/$', views.PostDetailAPIView.as_view(), name="post-detail-api"),
    url(r'^accounts/otherprofiles/(?P<pk>\d+)/$', views.PostDetailAPIView.as_view(), name="post-detail-api"),
    url(r'^accounts/myactivities/$', views.NotificationAPIView.as_view(), name="notificaition-self-api"),
    url(r'^accounts/marknoti_seen/(?P<pk>\d+)/$', views.NotificationSeenAPIView.as_view(), name="notification-mark-read"),
    #Er ikke så veldig sikker på om vi skal vise aktiviteten til andre brukere.
    #url(r'^accounts/otheractivities/(?P<pk>\d+)/$', views.NotificationAPIView.as_view(), name="notifications-other-api"),
]
