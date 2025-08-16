# clinica_odonto/agendamentos/views.py

from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import get_user_model # Importação corrigida
from django.shortcuts import get_object_or_404

# Crie uma variável para o modelo de usuário
User = get_user_model()

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    query = request.GET.get('q')

    if query:
        agendamentos = agendamentos.filter(
            Q(tipo_consulta__icontains=query) |
            Q(paciente__nome_completo__icontains=query) |
            Q(dentista__username__icontains=query) # Esta linha já estava correta, mas a importação é a chave
        ).distinct()

    context = {
        'agendamentos': agendamentos,
        'query': query,
    }
    return render(request, 'agendamentos/lista_agendamentos.html', context)


def cadastrar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento cadastrado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    
    context = {
        'form': form,
        'is_cadastro': True
    }
    return render(request, 'agendamentos/cadastro_agendamento.html', context)


# Nova view para edição de agendamentos
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)

    context = {
        'form': form,
        'is_cadastro': False, # Indica que o formulário é para edição
    }
    
def detalhes_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    context = {
        'agendamento': agendamento
    }
    return render(request, 'agendamentos/detalhes_agendamento.html', context)    
    
def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)

    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento excluído com sucesso!')
        return redirect('lista_agendamentos')

    context = {
        'agendamento': agendamento
    }
    return render(request, 'agendamentos/confirma_exclusao.html', context)

