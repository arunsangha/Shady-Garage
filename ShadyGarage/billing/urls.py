from django.conf.urls import url
from .import views
app_name = "billing"
urlpatterns = [
    url(r'^create/$', views.payment_method_createview, name="billing-create"),
]
