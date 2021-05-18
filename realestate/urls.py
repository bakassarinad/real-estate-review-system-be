"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import refresh_jwt_token
from users.api import RegisterApi, LoginJWT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/properties/', include('property.urls')),
    path('api/v1/images/', include('images.urls')),
    path('api/v1/profiles/', include('users.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/login/', LoginJWT.as_view()),
    path('api/v1/register', RegisterApi.as_view(), name='register'),
    path('api/v1/refresh', refresh_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
