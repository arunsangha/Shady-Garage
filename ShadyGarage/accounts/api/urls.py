from django.conf.urls import url
from rest_framework.authtoken import views
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name="register"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^api-token-auth/', views.obtain_auth_token, name="token-login"),
]
