from django.conf.urls import url
from .views import MeetsListAPIView
urlpatterns = [
    url(r'^$', MeetsListAPIView.as_view(), name="meets-list-api-view"),
]
