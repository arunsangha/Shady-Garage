from django.conf.urls import url
from .views import BlogDetail
urlpatterns = [
    url(r'detail/$', BlogDetail.as_view(), name="detail"),
]
