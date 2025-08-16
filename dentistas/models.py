# clinica_odonto/dentistas/models.py

from django.db import models
from django.urls import reverse

class Dentista(models.Model):
    nome_completo = models.CharField(max_length=200)
    CRO = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome_completo} ({self.especialidade})'

    def get_absolute_url(self):
        return reverse('detalhe_dentista', kwargs={'pk': self.pk})