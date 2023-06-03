# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProveedorForm, ProductoForm
from .models import Producto
from django.http import HttpResponse

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ("<h1>Agregado Correctamente</h1>")
    form = ProveedorForm()
    return render(request, 'actualizar_formulario.html', {
        'form': form,
        "submit": "agregar",
        })

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'actualizar_formulario.html', {
        'form': form,
        "submit": "agregar",
        })


