# clinica_odonto/agendamentos/forms.py

from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'dentista', 'data_hora', 'tipo_consulta', 'status', 'observacoes']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'dentista': forms.Select(attrs={'class': 'form-control'}), # Adicione esta linha
            'data_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'tipo_consulta': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'paciente': 'Paciente',
            'dentista': 'Dentista', # Adicione esta linha
            'data_hora': 'Data e Hora',
            'tipo_consulta': 'Tipo de Consulta',
            'status': 'Status',
            'observacoes': 'Observações',
        }