from django.shortcuts import render
from django.http import HttpResponse
from registro_familiar.models import Familia

# Create your views here.

def lista_familia(request):

    familia = Familia.objects.all()

    lista_familia_nombre = []

    for familia in Familia:  # type: ignore
        lista_familia_nombre.append(familia.nombre)
    
    return HttpResponse(lista_familia_nombre)
