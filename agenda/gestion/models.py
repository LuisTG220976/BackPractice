from contextlib import nullcontext
from email.policy import default
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Importancia (models.Model):
    id      = models.AutoField(primary_key=True, null=False)
    nombre  = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table='importancias'


class Tarea(models.Model):
    class CategoriaOpciones(models.TextChoices):
        LISTADO = ('LISTADO','LISTADO')
        POR_HACER = ('POR HACER','POR HACER')
        HACIENDO = ('FINALIZADO','FINALIZADO')
        CANCELADO = ('CANCELADO','CANCELADO')

    categoria = models.CharField(choices=CategoriaOpciones.choices, max_length=15,default='LISTADO')
    nombre=models.CharField(max_length=250,null=False)        
    descripcion=models.TextField(null=True)
    fechaCaducidad=models.DateTimeField(null=True)