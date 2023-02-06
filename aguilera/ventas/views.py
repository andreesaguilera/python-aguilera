from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Venta

""" 
def list_ventas(request):    
    all_ventas = Venta.objects.all()
    context = {
      'ventas': all_ventas
    }
    return render(request, 'ventas/list_ventas.html', context) 
"""

#Listar ventas con clase basada en vistas
class list_ventas(LoginRequiredMixin, ListView):
    model = Venta
    template_name = 'ventas/list_ventas.html'
    context_object_name = 'ventas'

""" 
def create_venta(request):
    if request.method == 'GET':      
      return render(request, 'ventas/create_venta.html', context={})

    else:
      print(request.POST)
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      antiguedad = request.POST.get('antiguedad')
      credito = request.POST.get('credito')
      imagen = request.POST.get('imagen')
      Venta.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, antiguedad = antiguedad, credito = credito, imagen = imagen)
      return render(request, 'ventas/create_venta.html', context={})
 """

 #Crear ventas con clase basada en vistas
class create_venta(CreateView):
    model = Venta
    template_name = 'ventas/create_venta.html'
    fields = ['nombre', 'precio', 'descripcion', 'antiguedad', 'credito', 'imagen']
    success_url = '/ventas/list-ventas/'

def update_venta(request, id):
    venta = Venta.objects.get(id = id)
    if request.method == 'GET':
      context = {
        'venta': venta
      }
      return render(request, 'ventas/edit_venta.html', context)
    else:
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      antiguedad = request.POST.get('antiguedad')
      credito = request.POST.get('credito')
      imagen = request.FILES.get('imagen')
      venta.nombre = nombre
      venta.precio = precio
      venta.descripcion = descripcion
      venta.antiguedad = antiguedad
      venta.credito = credito
      venta.imagen = imagen
      venta.save()
      return render(request, 'ventas/edit_venta.html', context={})

  #Eliminar ventas con clase basada en vistas
class delete_venta(DeleteView):
    model = Venta
    template_name = 'ventas/delete_venta.html'
    success_url = '/ventas/list-ventas/'
    context_object_name = 'venta'





