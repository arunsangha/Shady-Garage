from django.conf.urls import url
from .views import get_views
app_name = "analytics"

urlpatterns = [
    url(r'^$', get_views, name="views"),
]
