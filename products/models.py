from django.db import models


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    foto = models.URLField(max_length=500)

    class Meta:
        db_table = "product"
 

    def __str__(self):
        return self.titulo