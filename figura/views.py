from django.http import HttpRequest
from django.shortcuts import render
from .models import Carrusel , Figuras ,DetalleF
# Create your views here.
def index(request):
    carrusel = Carrusel.objects.all()
    figuras = Figuras.objects.all()
    context = {
        'carrusel': carrusel,
        'figuras': figuras
    }
    return render(request, 'figura/index.html', context)

def carrito(request):
    return render(request, 'figura/carrito.html')

def detalleF(request):
    detalle = DetalleF.objects.all()
    context ={
        'detalle':detalle
    }   
    return render(request, 'figura/detalleF.html',context)


def contacto(request):
    return render(request, 'figura/contacto.html')

def figura(request):
    figuras = Figuras.objects.all()
    context={
        'figuras': figuras
    }
    return render(request, 'figura/figura.html',context)

#Buscar FIGURA

def search(request):
    q = request.GET.get('q')  
    if q: 
        figuras = Figuras.objects.filter(nombreF__icontains=q)
        found_results = figuras.exists()  
    else:
        figuras = Figuras.objects.all()  
        found_results = True if figuras else False

    context = {
        'figuras': figuras,
        'query': q, 
        'found_results': found_results  
    }
    return render(request, 'figura/figura.html', context)


def registro(request):
    return render(request, 'figura/registro.html')

def iniciarsesion(request):
    return render(request, 'figura/iniciarsesion.html')  