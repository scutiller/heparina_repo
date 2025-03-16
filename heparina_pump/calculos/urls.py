from django.urls import path
from .views import calcular_bomba

urlpatterns = [
    path('', calcular_bomba, name='calcular_bomba'),
]
