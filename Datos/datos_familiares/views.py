from datetime import date
from django.forms import DateField
from django.http import HttpResponse
from django.template import Template, Context, loader


def familiares(request):

    datos = { "Madre": ("Carolina Lopez, Fecha de Nacimiento: 1967-12-20, Edad: 54"), "Padre": "Enrique Saracco, Fecha de Nacimiento: 1967-10-28, Edad: 54", "Hermana": "Rocio Saracco, Fecha de Nacimiento: 1995-11-21, Edad: 26" }

    plantilla = loader.get_template("familia.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)











