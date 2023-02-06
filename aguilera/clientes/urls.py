from django.urls import path
from .views import create_cliente, list_clientes, update_cliente, delete_cliente

urlpatterns = [
    path('create-cliente/', create_cliente.as_view()),
    path('list-clientes/', list_clientes.as_view()),
    path('edit-cliente/<int:id>', update_cliente),
    path('delete-cliente/<int:pk>', delete_cliente.as_view()),
]