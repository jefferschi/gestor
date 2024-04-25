from django.urls import path

#from portal.views import PaginaInicialView
from geesto.views import GeestoHomeView

urlpatterns = [
    path('', GeestoHomeView.as_view(), name='geesto-home'),

]