from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Incendio


class FireMap(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fires = Incendio.objects.filter(activo=True)
        print(len(fires))
        if len(fires) > 0:
            context['bo'] = True
            context['fires'] = fires
        else:
            context['bo'] = False
        return context
