from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField(unique=True)
    def _str_(self):
        return f"{self.nombre} {self.apellido}"
    
    @classmethod
    def buscar_por_correo(cls, correo):
        return cls.objects.filter(correo=correo).first()
    
class Estilos_Yoga(models.Model):
    estilo_1 = models.CharField(max_length=40)
    
class Horarios(models.Model):
    horario_posible = models.DateField()
    
