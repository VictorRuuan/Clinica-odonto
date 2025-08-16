# clinica_odonto/pacientes/admin.py

from django.contrib import admin
from .models import Paciente

# Opcional: Para personalizar como o Paciente aparece no admin
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'telefone', 'email', 'data_cadastro')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('data_cadastro',) # Permite filtrar por data de cadastro

admin.site.register(Paciente, PacienteAdmin)