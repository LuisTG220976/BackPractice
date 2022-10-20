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
    fechaCaducidad=models.DateTimeField(db_column='fecha_caducidad')
    #relaciones
    importancia = models.ForeignKey(to=Importancia, db_column='importancia_id', on_delete=models.PROTECT,null=False)

    class Meta:
        db_table ='tareas'


class Etiqueta(models.Model):
    #id      =   models.AutoField(primary_key=True, null=False)
    nombre  =   models.CharField(max_length=45, null=False, unique=True)
    #tarea   =   models.ForeignKey(to=Tarea, db_column='tarea_id', #on_delete=models.RESTRICT)

    class Meta:
        db_table ='etiquetas'

class TareaEtiquetas(models.Model):
    tarea   = models.ForeignKey(to=Tarea, db_column='tarea_id', on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(to=Etiqueta, db_column='etiqueta_id', on_delete=models.CASCADE)

    class Meta:
        db_table ='tareas_etiquetas'
             
