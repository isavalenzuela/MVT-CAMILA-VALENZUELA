from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

from AppPrimerMvt.models import Familia

def saludo (request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy fácil")

def probandoTemplate(self):
    miHtml = open("/Users/isavalenzuela/Desktop/MVT-CAMILAVALENZUELA/Proyecto1/plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def mi_familia(self):
    mama = Familia(nombre_completo = "Marcia", edad = 56, fecha_nac ='1966-08-09')
    # mama.save()
    documentoDeTexto1 =f"---> El nombre de mi mamá es: {mama.nombre_completo}, tiene {mama.edad} años y nació el {mama.fecha_nac}"

    papa =Familia(nombre_completo = "Danilo", edad = 59, fecha_nac = '1962-05-17')
    # papa.save()
    documentoDeTexto2 =f"---> El nombre de mi papá es: {papa.nombre_completo}, tiene {papa.edad} años y nació el {papa.fecha_nac}"

    hermano = Familia (nombre_completo = "Gaspar", edad = 23, fecha_nac='1998-12-29')
    # hermano.save()
    documentoDeTexto3 =f"---> El nombre de mi hermano es: {hermano.nombre_completo}, tiene {hermano.edad} años y nació el {hermano.fecha_nac}"

    finalText = documentoDeTexto1 + "\n" + documentoDeTexto2 + "\n" + documentoDeTexto3

    return HttpResponse(finalText)