from django.urls import path
from .views import create_alquiler, list_alquileres, update_alquiler, delete_alquiler

urlpatterns = [
    path('create-alquiler/', create_alquiler),
    path('list-alquileres/', list_alquileres),
    path('edit-alquiler/<int:id>', update_alquiler),
    path('delete-alquiler/<int:id>', delete_alquiler),

]