"""ShadyGarage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name = 'home'),
    url(r'^about/$', views.AboutPage.as_view(), name = 'about'),
    url(r'^accounts/', include('accounts.urls'), name = 'accounts'),
    url(r'^accounts/', include("django.contrib.auth.urls")),
    url(r'^meets/', include('meets.urls'), name = 'meets'),
    url(r'^posts/', include('posts.urls'), name = 'posts'),
    url(r'^blog/', include('blogs.urls'), name="blog"),
    url(r'^api/blog/', include('blogs.api.urls'), name="api-blog"),
    url(r'^analytics/', include('analytics.urls'), name="analytics"),
    url(r'^entertainment/', include('entertainments.urls'), name = "entertainments"),
    url(r'^api/posts/', include('posts.api.urls'), name="api-posts"),
    url(r'^api/meets/', include('meets.api.urls'), name="api-meets"),
    url(r'^api/entertainment/', include('entertainments.api.urls'), name="api-entertainments"),
    url(r'^api/accounts/', include('accounts.api.urls'), name="api-accounts"),
    url(r'^shop/', include('products.urls'), name="products"),
    url(r'^cart/', include('carts.urls'), name="carts"),
    url(r'^addresses/', include('addresses.urls'), name="addresses"),
    url(r'^billing/', include('billing.urls'), name="billing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #Setningen over virker kun under production, ikke deployment.
handler404 = views.error_404.as_view()
handler500 = views.error_500.as_view()
