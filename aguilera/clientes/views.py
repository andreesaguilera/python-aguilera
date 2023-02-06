from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from .models import Cliente

#Listar clientes con clase basada en vistas
class list_clientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/list_clientes.html'
    context_object_name = 'clientes'

#Crear cliente con clase basada en vistas
class create_cliente(CreateView):
    model = Cliente
    template_name = 'clientes/create_cliente.html'
    fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion', 'estado']
    success_url = '/clientes/list-clientes/'

def update_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'GET':
      context = {
        'cliente': cliente
      }
      return render(request, 'clientes/edit_cliente.html', context)
    else:
      nombre = request.POST.get('nombre')
      apellido = request.POST.get('apellido')
      telefono = request.POST.get('telefono')
      email = request.POST.get('email')
      direccion = request.POST.get('direccion')
      estado = request.POST.get('estado')
      cliente.nombre = nombre
      cliente.apellido = apellido
      cliente.telefono = telefono
      cliente.email = email
      cliente.direccion = direccion
      cliente.estado = estado
      cliente.save()
      return render(request, 'clientes/edit_cliente.html', context={})
    
#Eliminar cliente con clase basada en vistas
class delete_cliente(DeleteView):
    model = Cliente
    template_name = 'clientes/delete_cliente.html'
    success_url = '/clientes/list-clientes/'
    context_object_name = 'cliente'


    