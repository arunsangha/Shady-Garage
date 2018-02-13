from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^post_feed/$', views.PostList.as_view(), name="posts_feed"),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name="post_detail"),
    url(r'^new_post/$', views.PostForm.as_view(), name="post_create"),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name="post_delete"),
    url(r'^(?P<slug>[-\w]+)/comment/$', views.PostCommentCreateView.as_view(), name="post_comment"),
]
