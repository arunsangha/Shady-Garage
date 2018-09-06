from django.conf.urls import url
from . import views
app_name = "products"
urlpatterns = [
    url(r'^(?P<category>[-\w]+)/$', views.ProductList.as_view(), name="list"),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', views.ProductDetail.as_view(), name="detail"),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/custom_sticker/$', views.CustomSticker.as_view(), name="custom-sticker"),
]
