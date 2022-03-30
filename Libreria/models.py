from django.db import models

# Create your models here.

class Libros(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', null = True, verbose_name='imagen')
    descripcion = models.TextField(null=True, verbose_name='descripcion')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "libro"
        verbose_name_plural = "libros" 

    def __str__(self):

        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using = None, keep_parents = False):

        self.imagen.storage.delete(self.imagen.name)
        super().delete()

