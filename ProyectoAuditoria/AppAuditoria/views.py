from django.shortcuts import render
from django.http import HttpResponse
from .models import Auditor, Auditado, Sector, Entregable

#def vista_ejemplo(request):
#   return HttpResponse("Esta es una vista de ejemplo en AppAuditoria.")

def pagina_de_inicio(request):
    return render(request, 'AppAuditoria/index.html')

def listar_auditores(request):
    auditores = Auditor.objects.all()
    return render(request, 'appauditoria/lista_auditores.html', {'auditores': auditores})

def lista_auditados(request):
    auditados = Auditado.objects.all()
    return render(request, 'appauditoria/lista_auditados.html', {'auditados': auditados})

def lista_sectores(request):
    sectores = Sector.objects.all()
    return render(request, 'appauditoria/lista_sectores.html', {'sectores': sectores})

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'appauditoria/lista_entregables.html', {'entregables': entregables})




