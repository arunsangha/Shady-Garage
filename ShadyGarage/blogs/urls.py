from django.conf.urls import url
from .views import BlogDetail, BlogList

app_name = "blogs"
urlpatterns = [
    url(r'^$', BlogList.as_view(), name="list"),
    url(r'detail/(?P<slug>[-\w]+)/', BlogDetail.as_view(), name="detail"),
]
