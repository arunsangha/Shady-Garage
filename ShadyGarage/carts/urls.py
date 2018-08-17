from django.conf.urls import url
from .import views

app_name = "carts"
urlpatterns = [
    url(r'^$', views.cart_home, name="cart-home"),
    url(r'^add/(?P<pk>\d+)/$', views.cart_add, name="cart-add"),
]
