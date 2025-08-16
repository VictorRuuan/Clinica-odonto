# clinica_odonto/agendamentos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_agendamentos, name='lista_agendamentos'),
    path('cadastrar/', views.cadastrar_agendamento, name='cadastrar_agendamento'),
    path('editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
    # Nova URL para ver os detalhes de um agendamento
    path('detalhes/<int:pk>/', views.detalhes_agendamento, name='detalhes_agendamento'),
]