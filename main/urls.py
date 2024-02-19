from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('rooms/', include('rooms.urls')),
    path('clients/', include('clients.urls')),
    path('reservations/', include('reservations.urls')),
    path('biling/', include('biling.urls')),
]
