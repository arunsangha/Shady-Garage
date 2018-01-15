from django.conf.urls import url
from . import views

app_name = 'meets'

urlpatterns = [
    url(r'^$', views.MeetsListView.as_view(), name = 'meets_list'),
    url(r'^new/', views.CreateMeetView.as_view(), name = 'create_meet'),
    url(r'^@/(?P<slug>[-\w]+)/$', views.DetailMeetView.as_view(), name='single'),
]
