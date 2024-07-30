from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    
class Estilos_Yoga(models.Model):
    estilo_1 = models.CharField(max_length=40)
    
class Horarios(models.Model):
    horario_posible = models.DateField()

