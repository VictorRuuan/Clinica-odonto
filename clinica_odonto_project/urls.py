# clinica_odonto_project/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendamentos/', include('agendamentos.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('dentistas/', include('dentistas.urls')), # Adicione esta linha
    path('', core_views.dashboard_view, name='home'),
]