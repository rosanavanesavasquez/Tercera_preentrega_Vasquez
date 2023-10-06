"""
URL configuration for ProyectoAuditoria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppAuditoria/', include('AppAuditoria.urls')),
    
    #path('', views.pagina_de_inicio, name='pagina_de_inicio'),
    #path('auditores/', views.listar_auditores, name='lista_auditores'),
    #path('auditados/', views.lista_auditados, name='lista_auditados'),
    #path('sectores/', views.lista_sectores, name='lista_sectores'),
    #path('entregables/', views.lista_entregables, name='lista_entregables'),
]
