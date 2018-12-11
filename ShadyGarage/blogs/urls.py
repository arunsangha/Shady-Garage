from django.conf.urls import url
from .views import BlogDetail, BlogList
urlpatterns = [
    url(r'^$', BlogList.as_view(), name="list"),
    url(r'detail/$', BlogDetail.as_view(), name="detail"),
]
