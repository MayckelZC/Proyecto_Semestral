from django.shortcuts import render, redirect , get_object_or_404
from .forms import ContactoForm, FigurasForm, CustomUserCreationForm
from .models import Carrusel , Figuras 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from .cart import Carro

 

# Create your views here.

def index(request):
    carrusel = Carrusel.objects.all()
    figuras = Figuras.objects.filter(id__in=[1, 5, 7])
    context = {
        'carrusel': carrusel,
        'figuras': figuras
    }
    return render(request, 'figura/index.html', context)


def detalleF(request, slug):
    figuras = get_object_or_404(Figuras, slug=slug)
    figuras = [figuras]  

    context = {
        'figuras': figuras
    }

    return render(request, 'figura/detalleF.html', context)

  

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

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Registrado con Exito")           
            return redirect(to=index)
        context["form"] = formulario
    return render(request, 'registration/registrar.html',context)


@permission_required('figura.add_figuras')
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

@permission_required('figura.view_figuras')
def listar_figuras(request):
    figuras= Figuras.objects.all()
    context={
        'figuras' : figuras
    }
    return render(request, 'figura/adm/listar.html',context )
    
@permission_required('figura.change_figuras')
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

@permission_required('figura.delete_figuras')
def eliminar_figuras(request, id):
    figuras= get_object_or_404(Figuras, id=id)
    figuras.delete()
    messages.success(request, "Figura Eliminada con Exito")
    return redirect(to="listar_figuras")



def viewcart(request):
    carro = Carro(request)
    total_carro = carro.importe_total_carro()
    return render(request, 'figura/carrito.html', {'carro': request.session['carro'], 'total_carro': total_carro})

def agregar_producto(request, figura_id):
    carro = Carro(request)
    figura = Figuras.objects.get(id=figura_id)
    carro.agregar(figura=figura)
    carro.guardar_carro()  # Guardar el carro en la sesión

    return redirect(to="viewcart")

def eliminar_producto(request, figura_id):
    carro=Carro(request)
    figura=Figuras.objects.get(id=figura_id)
    carro.eliminar(figura=figura)
    return redirect(to="viewcart")


def restar_producto(request, figura_id):
    carro = Carro(request)
    figura = Figuras.objects.get(id=figura_id)
    carro.restar(figura=figura)
    return redirect(to="viewcart")



def importe_total_carro(request):
	total=0
	if request.user.is_authenticated:
		if "carro" in request.session:
			for key, value in request.session[""].items():
				total= total + int(value["precio"])
	return total


def procesar_compra(request):
    carro = Carro(request)
    carro.limpiar_carro()
    messages.success(request, 'Gracias por su Compra!!')

    return redirect(to='index')

def cleancart(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="viewcart")

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