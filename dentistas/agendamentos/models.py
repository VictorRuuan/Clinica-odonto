# clinica_odonto/agendamentos/models.py

from django.db import models
from pacientes.models import Paciente
from dentistas.models import Dentista  # Importa o modelo Dentista

class Agendamento(models.Model):
    TIPO_CHOICES = [
        ('avaliacao', 'Avaliação'),
        ('limpeza', 'Limpeza'),
        ('restauracao', 'Restauração'),
        ('extracao', 'Extração'),
        ('outros', 'Outros'),
    ]

    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dentista = models.ForeignKey(Dentista, on_delete=models.CASCADE) # Campo do dentista
    data_hora = models.DateTimeField()
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CHOICES, default='avaliacao')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendado')
    observacoes = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Agendamento de {self.paciente.nome_completo} com {self.dentista.nome_completo} em {self.data_hora.strftime("%d/%m/%Y %H:%M")}'

    class Meta:
        ordering = ['data_hora']