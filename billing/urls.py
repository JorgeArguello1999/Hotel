from django.urls import path

# Vistas
from billing import views

urlpatterns = [
    path('', views.billing, name='billing'),
    path('update/<int:id_billing>', views.billing_update, name='billing_update'),
    path('delete/<int:id_billing>', views.billing_delete, name='billing_delete'),
]