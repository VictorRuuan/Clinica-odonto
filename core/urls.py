# clinica_odonto/core/urls.py

from django.urls import path
from . import views # Importa as views do app core

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'), # URL para a página inicial
]