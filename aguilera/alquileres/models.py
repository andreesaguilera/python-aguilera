from django.db import models

class Alquiler(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    ambientes = models.IntegerField()
    expensas = models.BooleanField()
    """ imagen = models.CharField(max_length=200)   """
    imagen = models.ImageField(upload_to='alquiler_images', null=True, blank=True) #se debe instalar pillow  

    def __str__(self):
        return self.nombre