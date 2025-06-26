from django.db import models

class PuntoMonitoreo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    servicio = models.CharField(max_length=50, choices=[
        ('siesa', 'Siesa – POS PVD'),
        ('didi', 'Didi Food – Canales Digitales'),
        ('planta', 'Planta – Call Center'),
    ])
    latencia = models.FloatField()
    packet_loss = models.FloatField()
    jitter = models.FloatField()
    link = models.CharField(max_length=10)
    fecha = models.DateTimeField(auto_now_add=True)
