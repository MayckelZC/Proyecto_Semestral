from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'),
    path('detalleF',views.detalleF, name='detalleF'),
    path('contacto',views.contacto, name='contacto'),
    path('figura',views.figura, name='figura'),
    path('registro',views.registro, name='registro'),
    path('iniciarsesion',views.iniciarsesion, name='iniciarsesion'),
    path('search',views.search, name='search'),


]