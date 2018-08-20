from django.conf.urls import url
from .import views

app_name = "carts"
urlpatterns = [
    url(r'^$', views.cart_home, name="cart-home"),
    url(r'^add/(?P<pk>\d+)/$', views.cart_add, name="cart-add"),
    url(r'^checkout/$', views.cart_checkout, name="cart-checkout"),
    url(r'^checkout/confirm/$', views.cart_confirm, name="cart-confirm"),
]
