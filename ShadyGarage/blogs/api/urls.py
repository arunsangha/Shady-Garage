from django.conf.urls import url
from . import views

app_name = "blogs_api"

urlpatterns = (
    url(r'^$', views.BlogListAPIView.as_view(), name="list"),
)
