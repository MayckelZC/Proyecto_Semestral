from django.contrib import admin
from .models import Categoria, Material
from .models import Figuras
from.models import Contacto
from.models import Carrusel

# Register your models here.

   
class FigurasAdmin(admin.ModelAdmin):
    list_display = ["nombreF","precioF"]
    list_editable = ["precioF"]
    search_fields = ["nombreF"]

class DetallesFAdmin(admin.ModelAdmin):
    list_display = ["nombreDF","disponible","precioDF"]
    list_editable = ["precioDF","disponible"]
    search_fields = ["nombreDF"]

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","asunto","mensaje"]

admin.site.register(Categoria)
admin.site.register(Material)
admin.site.register(Figuras, FigurasAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Carrusel)