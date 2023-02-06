from django.urls import path
from .views import create_venta, list_ventas, update_venta, delete_venta

urlpatterns = [
    path('create-venta/', create_venta.as_view()),
    path('list-ventas/', list_ventas.as_view()),
    path('edit-venta/<int:id>', update_venta),
    path('delete-venta/<int:pk>', delete_venta.as_view()),
]