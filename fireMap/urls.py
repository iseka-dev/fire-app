from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        '',
        login_required(
            views.FireMap.as_view(),
            login_url='../login'
        )
    ),
    path(
        'load_cuarteles/',
        login_required(
            views.load_cuarteles,
            login_url='../login'
        )
    ),
    path(
        'fires/',
        views.fires
    ),
]
