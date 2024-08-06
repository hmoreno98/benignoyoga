from django.urls import path
from .views import *

urlpatterns = [
    path("benignoyoga", registro_estudiantes),
    path('buscar', buscar_estudiantes, name="buscar_estudiantes"),
]
