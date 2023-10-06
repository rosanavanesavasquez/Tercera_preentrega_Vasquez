from django.shortcuts import render
#from .models import TuModelo
from django.http import HttpResponse

def vista_ejemplo(request):
    return HttpResponse("Esta es una vista de ejemplo en AppAuditoria.")

from .models import Auditor

def listar_auditores(request):
    auditores = Auditor.objects.all()
    return render(request, 'appauditoria/lista_auditores.html', {'auditores': auditores})

#def consultar_datos(request):
#    datos = TuModelo.objects.all()  # Consulta todos los objetos de TuModelo
#    return render(request, 'tuapp/tuplantilla.html', {'datos': datos})

