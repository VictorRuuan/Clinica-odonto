# clinica_odonto/pacientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_pacientes, name='lista_pacientes'),
    path('cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('excluir/<int:pk>/', views.excluir_paciente, name='excluir_paciente'),
]

#path('lista/', ...): Define que esta view será acessível em /pacientes/lista/.

#name='lista_pacientes': O nome que usaremos para referenciar esta URL nos templates e views.