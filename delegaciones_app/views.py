import json
from datetime import datetime
from pathlib import Path

from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'


def _load_json(filename):
    file_path = DATA_DIR / filename
    with file_path.open('r', encoding='utf-8') as file:
        return json.load(file)


def _calcular_estado(solicitud):
    estado = solicitud.get('estado', '').strip().lower()
    if estado == 'realizado':
        return 'Realizado', 'success'
    if estado == 'en proceso':
        return 'En proceso', 'primary'
    if estado == 'pendiente':
        fecha_compromiso = datetime.strptime(solicitud.get('fecha_compromiso'), '%Y-%m-%d').date()
        hoy = datetime.now().date()
        if fecha_compromiso < hoy:
            return 'Alerta Roja por Vencimiento', 'danger'
        return 'Pendiente', 'warning'
    return 'Pendiente', 'warning'


def index(request):
    ejes = ['Seguridad', 'DISERCO', 'Gestión Social', 'Organizaciones Comunitarias']
    delegaciones = [
        'Centro', 'Rural', 'La Antena', 'La Pampa', 'Avenida del Mar', 'Las Compañías'
    ]
    return render(request, 'delegaciones_app/index.html', {
        'ejes': ejes,
        'delegaciones': delegaciones,
    })


def solicitudes(request):
    data = _load_json('solicitudes.json')
    solicitudes_lista = data.get('solicitudes', [])

    for solicitud in solicitudes_lista:
        solicitud['estado_display'], solicitud['estado_class'] = _calcular_estado(solicitud)
        solicitud['fecha_ingreso'] = datetime.strptime(solicitud['fecha_ingreso'], '%Y-%m-%d').strftime('%d-%m-%Y')
        solicitud['fecha_compromiso'] = datetime.strptime(solicitud['fecha_compromiso'], '%Y-%m-%d').strftime('%d-%m-%Y')

    contexto = {
        'solicitudes': solicitudes_lista,
        'total': len(solicitudes_lista),
        'pendientes': sum(1 for item in solicitudes_lista if item['estado_display'] == 'Pendiente'),
        'en_proceso': sum(1 for item in solicitudes_lista if item['estado_display'] == 'En proceso'),
        'alertas': sum(1 for item in solicitudes_lista if item['estado_display'] == 'Alerta Roja por Vencimiento'),
    }
    return render(request, 'delegaciones_app/solicitudes.html', contexto)


def delegacion_detalle(request, nombre):
    data = _load_json('solicitudes.json')
    solicitudes_delegacion = []
    for solicitud in data.get('solicitudes', []):
        if solicitud.get('delegacion') == nombre:
            solicitud['estado_display'], solicitud['estado_class'] = _calcular_estado(solicitud)
            solicitud['fecha_ingreso'] = datetime.strptime(solicitud['fecha_ingreso'], '%Y-%m-%d').strftime('%d-%m-%Y')
            solicitud['fecha_compromiso'] = datetime.strptime(solicitud['fecha_compromiso'], '%Y-%m-%d').strftime('%d-%m-%Y')
            solicitudes_delegacion.append(solicitud)

    return render(request, 'delegaciones_app/delegacion_detalle.html', {
        'nombre': nombre,
        'solicitudes': solicitudes_delegacion,
    })
