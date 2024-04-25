from django.urls import path

from portal.views import PaginaInicialView

urlpatterns = [
    path('',PaginaInicialView.as_view(),name='index'),    

]