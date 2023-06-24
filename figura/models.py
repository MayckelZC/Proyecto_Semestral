from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Categoria(models.Model):
    categoria     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
    
class Material(models.Model):
    material     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.material)    


class Figuras(models.Model):    
    imagenP = models.ImageField(upload_to="Posters", null=True)
    imagenF = models.ImageField(upload_to="Figuras", null=True)
    nombreF = models.CharField(max_length=50)
    slug    = AutoSlugField(populate_from='nombreF')
    precioF = models.IntegerField()
    anime   = models.CharField(max_length=100)
    tamano  = models.CharField(max_length=30)
    marca   = models.CharField(max_length=30)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    envio = models.CharField(max_length=15)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.nombreF)
    
class Contacto(models.Model):
    nombre          =models.CharField(max_length=30)
    email            =models.EmailField()
    asunto           =models.CharField(max_length=50)
    mensaje          =models.CharField(max_length=300)

    def __str__(self):
        return str(self.nombre)

class Carrusel(models.Model):
    imagenC = models.ImageField(upload_to="Carrusel",null=True)

    def __str__(self):
        return str(self.imagenC)