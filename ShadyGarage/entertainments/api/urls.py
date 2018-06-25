from django.conf.urls import url
from . import views

app_name = "api-entertainments"
urlpatterns = [
    url(r'^$', views.EntertainmentList.as_view(), name="list"),
    url(r'like/(?P<pk>\d+)/$', views.EntertainmentLikeToggle.as_view(), name="like"),
]
