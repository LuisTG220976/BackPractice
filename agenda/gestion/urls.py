from django.urls import path
from .views import PruebaApiView, endpointInicial, ImportanciasView

urlpatterns = [
    path('inicio', endpointInicial),
    path('prueba',PruebaApiView.as_view()),
    path('importancias', ImportanciasView.as_view())
]