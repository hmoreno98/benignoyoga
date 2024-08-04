
from django.shortcuts import render,redirect
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
            correo = form.cleaned_data['correo']
            user_exist = Estudiantes.objects.filter(correo=form.cleaned_data['correo']).exists()
            if user_exist:
                return HttpResponse('El estudiante ya esta registrado')
            else:
                guardado=Estudiantes.objects.create(nombre=nombre, apellido=apellido,correo=correo)
                Estudiantes.save(guardado)
            return redirect('formulario.html')
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
