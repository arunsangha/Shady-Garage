from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^post_feed/$', views.PostList.as_view(), name="posts_feed"),
    url(r'^shady/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name="post_detail"),
    url(r'^new_post/$', views.PostForm.as_view(), name="post_create"),
    url(r'^shady/(?P<slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name="post_delete"),
    url(r'^shady/(?P<slug>[-\w]+)/comment/$', views.PostCommentCreateView.as_view(), name="post_comment"),
    url(r'^shady/(?P<slug>[-\w]+)/comment/(?P<pk>\d+)/delete/$', views.PostCommentDeleteView.as_view(), name="post_comment_delete"),
    url(r'^shady/(?P<slug>[-\w]+)/update/$', views.PostUpdateView.as_view(), name="post_update"),
    url(r'^shady/(?P<slug>[-\w]+)/faaaaiilll!/$', views.PostUpdateFail.as_view(), name="post_update_fail"),
]
