from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class Cuartel(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    jurisdiccion = models.PolygonField(blank=True, null=True)
    cuarteles_limitrofes = models.ManyToManyField('self', blank=True)
    fuego_activo = models.BooleanField()


class Incendio(models.Model):

    TIPOS_ESTADO = {
        'EN CURSO',
        'CONTROLADO',
        'CONTENIDO',
        'GUARDIA DE CENIZAS',
        'EXTINGUIDO',
        'REINICIO',
    }

    TIPOS_CARACTERISTICA = {
        '10-10 - INCENDIO FORESTAL',
        '10-11 - INCENDIO DE VALDIO',
        '10-12 - INCENDIO DE QUINCHO',
        '10-13 - INCENDIOINCENDIO EXTRUCTURAL',
        '10-14 - INCENDIO DE VEHICULO',
        '10-15 - INCENDIO FABRIL',
        '10-16 - ESCAPE DE GAS',
        '10-17 - DERRAME DE COMBUSTIBLE',
        '10-18 - INCIDENTE CON SUSTANCIAS PELIGROSAS',
        '10-19 - INCIDENTES CON ANIMALES E INSECTOS'
    }

    coordenadas = models.PointField(blank=True, null=True)
    estado = models.CharField(max_length=50)
    caracteristica = models.CharField(max_length=50)
    fecha_hora_inicio = models.DateTimeField(null=True, blank=True)  # empty field?
    # fecha_hora_extincion = models.DateTimeField(blank=True, null=True)
    radio = models.FloatField()  # extent
    cuarteles_afectados = models.ForeignKey(
        Cuartel,
        on_delete=models.RESTRICT
    )
    bomberos_afectados = models.IntegerField(null=True, blank=True)
    unid_livianas_afectadas = models.IntegerField(null=True, blank=True)
    unid_pesadas_afectadas = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(null=True, blank=True)  # marcador para mapa
    riesgo_interfase = models.BooleanField(null=True, blank=True)
