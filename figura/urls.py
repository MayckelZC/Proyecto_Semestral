from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('detalleF/<slug>/',views.detalleF, name='detalleF'),
    path('contacto',views.contacto, name='contacto'),
    path('figura',views.figura, name='figura'),
    path('registro',views.registro, name='registro'),
    path('search',views.search, name='search'),
    path('agregar_figura',views.agregar_figura, name='agregar_figura'),
    path('listar_figuras',views.listar_figuras, name='listar_figuras'),
    path('modificar_figuras/<id>/',views.modificar_figuras, name='modificar_figuras'),
    path('eliminar_figuras/<id>/',views.eliminar_figuras, name='eliminar_figuras'),
    path('viewcart', views.viewcart, name="viewcart"),
    path('addcart/<figura_id>/', views.agregar_producto, name="addcart"),
    path('delcart/<figura_id>/', views.eliminar_producto, name="delcart"),
    path('restarcart/<figura_id>/', views.restar_producto, name="restarcart"),
    path('procesar_compra', views.procesar_compra, name="procesar_compra"),
    path('cleancart', views.cleancart, name="cleancart"),

]