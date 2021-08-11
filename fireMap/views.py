from django.views.generic import TemplateView
from .models import Incendio, Cuartel
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from pathlib import Path
from zipfile import ZipFile
from django.contrib.gis.gdal import DataSource
from django.http import HttpResponse
from django.contrib.gis.utils import LayerMapping


class FireMap(TemplateView):
    template_name = "../templates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fires = Incendio.objects.filter(activo=True)
        if len(fires) > 0:
            context['bo'] = True
            context['fires'] = fires
            context['fire_locations'] = serialize(
                'geojson',
                fires
            )
        return context


@csrf_exempt
def fires(request):
    fires = Incendio.objects.filter(activo=True)
    fires = serialize('geojson', fires)
    return JsonResponse({'fires': fires})


@csrf_exempt
def load_cuarteles(request):
    mapping_cuartel = {
        'jurisdiccion': 'POLYGON',
        'nombre': 'Cuartel'
    }
    lm = LayerMapping(
        Cuartel,
        'staticfiles/Jurisdicciones',
        mapping_cuartel,
        transform=True
    )
    lm.save(verbose=True, strict=True)
    cuarteles = Cuartel.objects.all()
    len(cuarteles)
    for cuartel in cuarteles:
        fig = cuartel.jurisdiccion
        lims = Cuartel.objects.filter(jurisdiccion__touches=fig)
        cuartel.cuarteles_limitrofes.set(lims)
    return HttpResponse("Informacion de Tiempo Severo procesada")
