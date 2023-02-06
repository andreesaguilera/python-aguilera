from django.contrib import admin
from alquileres.models import Alquiler
from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'birth_date')    


@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'ambientes', 'expensas', 'imagen')
    list_filter = ('nombre', 'precio', 'descripcion', 'ambientes', 'expensas', 'imagen')
    search_fields = ('nombre', 'precio', 'descripcion', 'ambientes', 'expensas', 'imagen')
    ordering = ('nombre', 'precio', 'descripcion', 'ambientes', 'expensas', 'imagen')
    
