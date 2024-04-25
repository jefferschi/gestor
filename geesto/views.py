from django.shortcuts import render

from django.views.generic import TemplateView

class GeestoHomeView(TemplateView):
    template_name = 'geesto/home.html'