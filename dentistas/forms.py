# clinica_odonto/dentistas/forms.py

from django import forms
from .models import Dentista

class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista
        fields = ['nome_completo', 'CRO', 'especialidade', 'email', 'telefone', 'ativo']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'CRO': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome_completo': 'Nome Completo',
            'CRO': 'CRO',
            'especialidade': 'Especialidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'ativo': 'Ativo',
        }