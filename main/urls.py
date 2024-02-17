"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# JWT
from rest_framework_simplejwt import views as jwt_views
# Docs
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Vistas normales
    path('', include('home.urls')),
    path('admin/', admin.site.urls),

    # API
    path('api/rooms/', include("rooms.urls")),
    path('api/clients/', include("clients.urls")),
    path('api/reservations/', include("reservations.urls")),

    # Docs
    path('docs/', include_docs_urls('Hotel API')),

    # JWT
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]