from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre


class Category(models.Model):
    nombre = models.CharField(max_length=200, default="")
    descripcion = models.TextField(max_length=300, default="")

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    def url(self, filename):
        ruta = "MultimediaData/Producto/{}/{}"
        return ruta.format(self.nombre, self.nombre)

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to=url, default='', null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default='')
    caregoria = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return self.nombre


