from django.conf.urls import url

from . import views
app_name = "entertainments"

urlpatterns = [
    url(r'^$',views.EntertainmentList.as_view(), name="list"),
    url(r'^create/', views.EntertainmentCreate.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', views.EntertainmentUpdate.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.EntertainmentDelete.as_view(), name="delete"),
]
