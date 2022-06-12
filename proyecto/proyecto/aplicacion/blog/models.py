from django.db import models

# Create your models here.
class blog(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    autor = models.CharField(max_length=200)
    fecha_de_cargar = models.DateField(auto_now=True)
    def __str__(self):
        tex = "{0} ({1})"
        return tex.format(self.titulo,self.fecha_de_cargar)
