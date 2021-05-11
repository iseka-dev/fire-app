import json
from django.http import JsonResponse
from fireMap.models import Cuartel
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from fireMap.models import Incendio


@require_POST
@csrf_exempt
def status_cuartel(request):
    received_json = json.loads(request.body)
    token = received_json.get('token')
    user = get_object_or_404(Token, key=token).user
    cuartel = user.cuartel
    if cuartel.fuego_activo is True:
        color = '#F7B902'
    elif cuartel.fuego_activo is False:
        if Cuartel.objects.filter(
            fuego_activo=True,
            cuarteles_limitrofes=cuartel,
        ):
            color = '#F30202'
        else:
            color = '#8fd9a8'
    return JsonResponse({'color': color})


@require_POST
@csrf_exempt
def confirmar_incendio(request):
    received_json = json.loads(request.body)
    token = received_json.get('token')
    user = get_object_or_404(Token, key=token).user
    cuartel = user.cuartel
    if received_json.get('falso_positivo') is True:
        return JsonResponse(
            {
                'Response':
                'El incendio denunciado es un falso_positivo'
            }
        )
    else:
        params = {
            'coordenadas': received_json.get('coordenadas'),
            'radio': received_json.get('radio'),
            'riesgo_interfase': received_json.get('riesgo_interfase'),
            'cuarteles_afectados': cuartel
        }
    incendio = Incendio(**params)
    incendio.save()
    return JsonResponse(
        {
            'Response':
            'El incendio ha sido confirmado y agregado a la base de datos'
        }
    )


@require_POST
@csrf_exempt
def informar_incendio(request):
    received_json = json.loads(request.body)
    token = received_json.get('token')
    user = get_object_or_404(Token, key=token).user
    cuartel = user.cuartel
    params = {
        'coordenadas': received_json.get('coordenadas'),
        'radio': received_json.get('radio'),
        'riesgo_interfase': received_json.get('riesgo_interfase'),
        'cuarteles_afectados': cuartel,
        'estado': received_json.get('estado'),
        'caracteristica': received_json.get('caracteristica'),
        'bomberos_afectados': received_json.get('bomberos_afectados'),
        'unid_pesadas_afectadas': received_json.get('unid_pesadas_afectadas'),
        'unid_livianas_afectadas': received_json.get(
            'unid_livianas_afectadas'
        ),
    }
    incendio = Incendio(**params)
    incendio.save()
    return JsonResponse(
        {
            'Response':
            'El incendio ha sido confirmado y agregado a la base de datos'
        }
    )
