from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='listar_productos'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
]