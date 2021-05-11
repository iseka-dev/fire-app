from django.urls import path
from . import views


urlpatterns = [
    path(
        'status_cuartel',
        views.status_cuartel,
        name='status_cuartel'
    ),
    path(
        'confirmar_incendio',
        views.confirmar_incendio,
        name='confirmar_incendio'
    ),
    path(
        'informar_incendio',
        views.informar_incendio,
        name='informar_incendio'
    ),
]
