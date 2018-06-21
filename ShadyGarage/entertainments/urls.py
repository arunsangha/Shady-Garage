from django.conf.urls import url

from . import views
app_name = "entertainments"

urlpatterns = [
    url(r'^$',views.EntertainmentList.as_view(), name="list"),
    url(r'^create/', views.EntertainmentCreate.as_view(), name="create"),
]
