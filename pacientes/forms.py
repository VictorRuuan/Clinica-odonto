# clinica_odonto/pacientes/forms.py
from django import forms
from .models import Paciente 

GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('N', 'Prefiro não informar'),
]

class PacienteForm(forms.ModelForm):
    genero = forms.ChoiceField(
        choices=GENERO_CHOICES,
        required=False, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Data de Nascimento",
        required=True
    )

    class Meta:
        model = Paciente
        fields = [
            'nome_completo', 'cpf', 'data_nascimento', 'genero',
            'telefone', 'email', 'endereco',
        ]
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'nome_completo': 'Nome Completo',
            'cpf': 'CPF',
            'genero': 'Gênero',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'endereco': 'Endereço Completo',
        }
        error_messages = {
            'cpf': {
                'unique': "Este CPF já está cadastrado.",
            },
        }