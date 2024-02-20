from django.urls import path

# Vistas
from billing import views

urlpatterns = [
    path('', views.billing, name='billing'),
    path('delete/<int:id_billing>', views.billing_delete, name='billing_delete'),
]