from django.urls import path
from . import views
from users import views as users_views


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
    path(
        'login',
        users_views.user_login,
        name='login'
    ),
    path(
        'logout',
        users_views.user_logout,
        name='logout'
    ),
]
