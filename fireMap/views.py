from django.views.generic import TemplateView
from .models import Incendio
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from pathlib import Path
from zipfile import ZipFile
from django.contrib.gis.gdal import DataSource


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
def load(request):
    ds = DataSource('/path/to/your/cities.shp')

    mapping_tiempo_severo = {
        'poly': 'MULTIPOLYGON',
        'pts': 'pts',
    }
    lm2 = LayerMapping(
        TiempoSevero,
        tempdir,
        mapping_tiempo_severo,
        transform=False
    )
    lm2.save(verbose=True, strict=True)
    return HttpResponse("Informacion de Tiempo Severo procesada")
