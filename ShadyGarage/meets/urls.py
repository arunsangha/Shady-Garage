from django.conf.urls import url
from . import views

app_name = 'meets'

urlpatterns = [
    url(r'^$', views.MeetsListView.as_view(), name = 'meets_list'),
]
