from django.contrib import admin
from ventas.models import Venta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'antiguedad', 'credito', 'imagen')
    list_filter = ('nombre', 'precio', 'descripcion', 'antiguedad', 'credito', 'imagen')
    search_fields = ('nombre', 'precio', 'descripcion', 'antiguedad', 'credito', 'imagen')
    ordering = ('nombre', 'precio', 'descripcion', 'antiguedad', 'credito', 'imagen')
  
    