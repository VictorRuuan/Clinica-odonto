from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # campos adicionais para o usuario, se necessário.
    # Por exemplo, um campo para "role" (papel) pode ser útil aqui
     # mas por enquanto, vamos usar o is_staff/is_superuser padrão do Django
    # para diferenciar recepcionistas/dentistas de administradores.
    # Ou poderíamos adicionar um campo 'cargo' = models.CharField(...)
    # Para o propósito deste projeto de portfólio, o AbstractUser já é suficiente
    # para a diferenciação de acesso via grupos do Django Admin.
    pass

    def __str__(self):
        return self.username