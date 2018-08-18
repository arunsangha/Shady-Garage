from django.conf.urls import url
from . import views
app_name="addresses"
urlpatterns = [
    url(r'^create_address/$', views.create_address, name="create-address"),
]
