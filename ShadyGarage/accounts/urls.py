from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name = "logout"),
    url(r'^signup_del2/$', views.ProfileInfo.as_view(), name = "signup_del2"),
    url(r'^myprofile/$', login_required(views.ProfilePage.as_view()), name="profile_page"),
    url(r'^otherprofiles/(?P<pk>\d+)/$', views.view_profiles, name="profile_page_pk"),
    url(r'^myprofile/edit/$', views.edit_profile, name="profile_edit"),
    url(r'^myprofile/change-password/$', views.change_password, name="change_password"),
    url(r'^activities/$', views.ProfileActivity, name="activity"),
    url(r'^otherprofiles/(?P<pk>\d+)/activities/$', views.ProfileActivity, name="activity-otherprofile-pages"),
    #if user has forgotten password
    url(r'^reset-password/$', auth_views.password_reset,{'template_name': 'accounts/reset_password.html',
        'post_reset_redirect':'accounts:password_reset_done', 'email_template_name':'accounts/reset_password_email.html'}
        , name="reset_password"),
    url(r'^reset-password/done/$', auth_views.password_reset_done,
        {'template_name':'accounts/reset_password_done.html'}, name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name':'accounts/password_reset_confirm.html', 'post_reset_redirect':'accounts:password_reset_complete'}
        ,name="password_reset_confirm"),
    url(r'^reset-password/complete/$', auth_views.password_reset_complete,
        {'template_name':'accounts/password_reset_complete.html'}, name="password_reset_complete"),
]
