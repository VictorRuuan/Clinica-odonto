# clinica_odonto/core/views.py

from django.shortcuts import render
from datetime import date, timedelta
from pacientes.models import Paciente
from agendamentos.models import Agendamento

def dashboard_view(request):
    # --- Dados Reais do Dashboard ---

    # Contar o número total de pacientes
    total_pacientes = Paciente.objects.count()

    # Contar agendamentos para hoje e o total
    hoje = date.today()
    total_agendamentos_hoje = Agendamento.objects.filter(data_hora__date=hoje).count()
    total_agendamentos = Agendamento.objects.filter(data_hora__date__gte=hoje).count()

    # --- Dados Reais para o Gráfico de Agendamentos por Semana ---
    # Inicializa um dicionário para armazenar a contagem por dia
    agendamentos_por_dia = {}
    # Lista com os próximos 7 dias a partir de hoje
    dias_da_semana = []

    for i in range(7):
        dia = hoje + timedelta(days=i)
        # Formato da data para o rótulo do gráfico
        label_dia = dia.strftime('%a, %d/%m')  # Ex: Ter, 15/08
        dias_da_semana.append(label_dia)

        # Conta os agendamentos para o dia
        contagem = Agendamento.objects.filter(data_hora__date=dia).count()
        agendamentos_por_dia[label_dia] = contagem

    # Dados para o contexto do template
    agendamentos_semanais_labels = dias_da_semana
    agendamentos_semanais_data = list(agendamentos_por_dia.values())

    # --- Dados Fictícios para a próxima consulta (por enquanto)
    proxima_consulta_info = {
        'paciente': 'Maria Eduarda',
        'hora': '15:00',
        'tipo': 'Restauração'
    }

    context = {
        'total_pacientes': total_pacientes,
        'total_agendamentos_hoje': total_agendamentos_hoje,
        'total_agendamentos': total_agendamentos,
        'proxima_consulta_info': proxima_consulta_info,
        'agendamentos_semanais_labels': agendamentos_semanais_labels,
        'agendamentos_semanais_data': agendamentos_semanais_data,
    }
    return render(request, 'core/dashboard.html', context)