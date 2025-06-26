from django.shortcuts import render
from .models import PuntoMonitoreo

def home (request):
    return render(request, 'home.html')

def monitoreo(request):
    return render(request, 'monitoreo.html')

def checklist(request):
    return render(request, 'checklist.html')

def siesa(request):
    return render(request, 'siesa.html')

def rappi(request):
    return render(request, 'rappi.html')

def didi(request):
    return render(request, 'didi.html')

def planta(request):
    return render(request, 'planta.html')


from django.shortcuts import render
from .models import PuntoMonitoreo

def monitoreo(request):
    datos = PuntoMonitoreo.objects.all().order_by('-fecha')  # O la columna de fecha que tengas

    # Agrupar por servicio
    servicios = ['Siesa', 'Didi Food', 'Planta']
    datos_por_servicio = []

    for servicio in servicios:
        puntos = datos.filter(servicio=servicio)
        grupo = {
            'servicio': servicio,
            'puntos': []
        }
        for punto in puntos:
            alerta = punto.latencia > 100 or punto.packet_loss > 2 or punto.jitter > 5 or punto.link == 'down'
            grupo['puntos'].append({
                'nombre': punto.nombre,
                'fecha': punto.fecha,
                'latencia': punto.latencia,
                'packet_loss': punto.packet_loss,
                'jitter': punto.jitter,
                'link': punto.link,
                'estado': 'Correcto' if not alerta else 'Con Fallos',
                'alerta': alerta
            })
        datos_por_servicio.append(grupo)

    return render(request, 'monitoreo.html', {'datos_por_servicio': datos_por_servicio})
