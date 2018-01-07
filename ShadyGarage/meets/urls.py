from django.conf.urls import url
from . import views

app_name = 'meets'

urlpatterns = [
    url(r'^$', views.MeetsListView.as_view(), name = 'meets_list'),
<<<<<<< HEAD
=======
    url(r'^new/', views.CreateMeetView.as_view(), name = 'create_meet'),
>>>>>>> a8c4cfe7bdf32f17e62d97c794696e0679bb462b
]
