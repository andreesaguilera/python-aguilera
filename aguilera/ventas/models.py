from django.db import models

class Venta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    antiguedad = models.IntegerField()
    credito = models.BooleanField()
    imagen = models.ImageField(upload_to='alquiler_images', null=True, blank=True) #se debe instalar pillow    

    def __str__(self):
        return self.nombre