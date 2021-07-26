from django.contrib import admin
from .models import Cuartel, Incendio


"""class FirePoint(admin.ModelAdmin):
    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }"""

admin.site.register(Cuartel)
admin.site.register(Incendio)
