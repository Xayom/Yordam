"""yordam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from user.views import RegisterFormView
from user.views import LoginFormView
from home.views import home
from django.conf import settings
from django.conf.urls.static import static
from post.views import add
from user.views import user_logout

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'register/', RegisterFormView.as_view(), name='register'),
    path(r'login/', LoginFormView.as_view(), name='login'),
    path(r'', home, name='home'),
    path(r'add', add, name='add'),
    path(r'thanks', home, name='thanks'),
    path(r'post/', include('post.urls')),
    path(r'logout/', user_logout, name='logout')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
