# clinica_odonto/dentistas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_dentistas, name='lista_dentistas'),
    path('cadastrar/', views.cadastrar_dentista, name='cadastrar_dentista'),
    path('<int:pk>/editar/', views.editar_dentista, name='editar_dentista'),
    path('<int:pk>/excluir/', views.excluir_dentista, name='excluir_dentista'),
]