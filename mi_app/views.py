#from django.shortcuts import render
#from django.http import HttpResponse
#from .models import *

#def BenignoYoga(request):
    #return HttpResponse("Benigno Yoga Scholl.... Loading")

# Create your views here.

#def lista_Estudiantes(request):
#   estudiates = Estudiantes.objects.all().order_by('nombre')
#  return render(request,'estudiantes/lista.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def BenignoYoga(request):
    return render(request, 'formulario.html')


def registro_estudiantes(request):
    if request.method == 'POST':
        form = EstudiantesForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
    else:    
        form = EstudiantesForm()

    return render(request, 'formulario.html', {'form': form})


def buscar_estudiantes(request):
    form = BuscarForm()
    resultados = []
    
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Estudiantes.objects.filter(email__icontains=query)
    
    return render(request, 'buscar_estudiantes.html', {'form': form, 'resultados': resultados})
