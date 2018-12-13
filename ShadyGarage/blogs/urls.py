from django.conf.urls import url
from .views import BlogDetail, BlogList, user_vote

app_name = "blogs"
urlpatterns = [
    url(r'^$', BlogList.as_view(), name="list"),
    url(r'detail/(?P<slug>[-\w]+)/', BlogDetail.as_view(), name="detail"),
    url(r'vote/$', user_vote, name="vote"),
]
