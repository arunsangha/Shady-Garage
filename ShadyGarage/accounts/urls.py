from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name = "logout"),
    url(r'^signup_del2/$', views.ProfileInfo.as_view(), name = "signup_del2"),
    url(r'^myprofile/$',views.ProfilePage.as_view(), name="profile_page"),
    url(r'^myprofile/edit/$', views.edit_profile, name="profile_edit"),
]
