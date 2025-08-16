# clinica_odonto/agendamentos/admin.py

from django.contrib import admin
from .models import Agendamento

# Opcional: Para personalizar como o Agendamento aparece no admin
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'dentista', 'data_hora', 'tipo_consulta', 'status', 'data_criacao')
    list_filter = ('status', 'dentista', 'tipo_consulta', 'data_hora')
    search_fields = ('paciente__nome_completo', 'dentista__username', 'tipo_consulta') # Busca em campos relacionados
    raw_id_fields = ('paciente', 'dentista') # Melhora a seleção de FKs quando há muitos registros

admin.site.register(Agendamento, AgendamentoAdmin)
