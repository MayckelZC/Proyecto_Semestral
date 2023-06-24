from django.shortcuts import render, redirect , get_object_or_404
from .forms import ContactoForm, FigurasForm, CustomUserCreationForm
from .models import Carrusel , Figuras 
from django.contrib import messages
from django.contrib

# Create your views here.

def index(request):
    carrusel = Carrusel.objects.all()
    figuras = Figuras.objects.filter(id__in=[1, 5, 7])
    context = {
        'carrusel': carrusel,
        'figuras': figuras
    }
    return render(request, 'figura/index.html', context)

def carrito(request):
    return render(request, 'figura/carrito.html')

def detalleF(request, slug):
    figuras = get_object_or_404(Figuras, slug=slug)
    figuras = [figuras]  

    context = {
        'figuras': figuras
    }

    return render(request, 'figura/detalleF.html', context)


def contacto(request):
    data ={
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Contacto Guardado"
        else:
            data["form"] = formulario    
    return render(request, 'figura/contacto.html', data)    

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
    context={
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST'
        formulario = CustomUserCreationForm(context=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=index)
        context["form"] = formulario
    return render(request, 'registration/registrar.html',context)


def agregar_figura(request):
    context={
        'form': FigurasForm()
    }
    if request.method == 'POST':
        formulario= FigurasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Figura Agregada con Exito")
        else:
            context["form"] = formulario
    return render(request, 'figura/adm/agregar.html',context)

def listar_figuras(request):
    figuras= Figuras.objects.all()
    context={
        'figuras' : figuras
    }
    return render(request, 'figura/adm/listar.html',context )

def modificar_figuras(request, id):
    figura = get_object_or_404(Figuras, id=id)

    if request.method == 'POST':
        formulario = FigurasForm(data=request.POST, instance=figura, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Figura Modificada con Exito")
            return redirect('listar_figuras')
    else:
        formulario = FigurasForm(instance=figura)

    context = {
        'form': formulario,
        'figuras': figura,  # Añade 'figuras' al contexto
    }

    return render(request, 'figura/adm/modificar.html', context)

def eliminar_figuras(request, id):
    figuras= get_object_or_404(Figuras, id=id)
    figuras.delete()
    messages.success(request, "Figura Eliminada con Exito")
    return redirect(to="listar_figuras")

    