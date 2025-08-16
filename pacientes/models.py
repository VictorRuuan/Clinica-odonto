from django.db import models

# Create your models here.
# clinica_odonto/pacientes/models.py

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True) # Ex: XXX.XXX.XXX-XX
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    historico_medico = models.TextField(blank=True, null=True, help_text="Alergias, doenças preexistentes, etc.")
    data_cadastro = models.DateTimeField(auto_now_add=True) # Registra a data de criação automaticamente

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome_completo'] # Ordena os pacientes por nome por padrão