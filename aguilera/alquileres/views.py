from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Alquiler

@login_required
def list_alquileres(request):
    """ if search """
    if 'search' in request.GET:      
      all_alquileres = Alquiler.objects.filter(nombre__icontains = request.GET.get('search'))
    else:
      all_alquileres = Alquiler.objects.all()    
    
    context = {
      'alquileres': all_alquileres
    }
    return render(request, 'alquileres/list_alquileres.html', context)

@login_required
def create_alquiler(request):
    if request.method == 'GET':      
      return render(request, 'alquileres/create_alquiler.html', context={})

    else:      
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      ambientes = request.POST.get('ambientes')
      expensas = request.POST.get('expensas')
      imagen = request.FILES.get('imagen')
      Alquiler.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, ambientes = ambientes, expensas = expensas, imagen = imagen)
      return render(request, 'alquileres/create_alquiler.html', context={})

@login_required
def update_alquiler(request, id):
    alquiler = Alquiler.objects.get(id = id)
    if request.method == 'GET':
      context = {
        'alquiler': alquiler
      }
      return render(request, 'alquileres/edit_alquiler.html', context)
    else:
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      ambientes = request.POST.get('ambientes')
      expensas = request.POST.get('expensas')
      imagen = request.FILES.get('imagen')
      alquiler.nombre = nombre
      alquiler.precio = precio
      alquiler.descripcion = descripcion
      alquiler.ambientes = ambientes
      alquiler.expensas = expensas
      alquiler.imagen = imagen
      alquiler.save()
      return render(request, 'alquileres/edit_alquiler.html', context={})

@login_required
def delete_alquiler(request, id):

    if request.method == 'GET':
      alquiler = Alquiler.objects.get(id = id)
      context = {
        'alquiler': alquiler
      }
      return render(request, 'alquileres/delete_alquiler.html', context)
    else:
      alquiler = Alquiler.objects.get(id = id)
      alquiler.delete()
      return render(request, 'alquileres/delete_alquiler.html', context={})







