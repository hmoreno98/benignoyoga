from django.urls import path
from .views import *

urlpatterns = [
    path("benignoyoga", BenignoYoga),
    path('', registro_estudiantes),
]
