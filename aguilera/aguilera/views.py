from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request, 'index.html', context={})

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def vista_con_edad(request, edad):
    return HttpResponse(f"Tu edad es {edad}")
     
def vista_con_template(request):
    return render(request, 'prueba.html')

def contex_1(request):
    nombre = "Andres"
    arr_1 = [1,2,3,4,5]
    context = {
      'nombre': nombre,
      'arr_1': arr_1
    }
    return render(request, 'contex_1.html', context)

def about(request):
    return render(request, 'about/about.html')