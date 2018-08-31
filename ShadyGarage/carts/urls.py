from django.conf.urls import url
from .import views

app_name = "carts"
urlpatterns = [
    url(r'^$', views.cart_home, name="cart-home"),
    url(r'^add/(?P<pk>\d+)/$', views.cart_add, name="cart-add"),
    url(r'^add-tshirt/(?P<pk>\d+)/(?P<size>[-\w]+)/$', views.cart_add_tshirt, name="cart-add-thirt"),
    url(r'^checkout/$', views.cart_checkout, name="cart-checkout"),
    url(r'^checkout/confirm/$', views.cart_confirm, name="cart-confirm"),
    url(r'^success/$', views.CartSuccess.as_view(), name="cart-success"),
]
