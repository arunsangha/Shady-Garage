from django.conf.urls import url
from . import views

app_name = 'meets'

urlpatterns = [
    url(r'^$', views.MeetsListView.as_view(), name = 'meets_list'),
    url(r'^new/', views.CreateMeetView.as_view(), name = 'create_meet'),
    url(r'^@/(?P<slug>[-\w]+)/$', views.DetailMeetView.as_view(), name='single'),
    url(r'^@/(?P<slug>[-\w]+)/like/$', views.MeetJoinToggleView.as_view(), name='join_meet'),
    url(r'^@/(?P<slug>[-\w]+)/comment/$', views.CommentMeetView.as_view(), name='comment_meet'),
]
