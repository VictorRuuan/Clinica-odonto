# clinica_odonto/pacientes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Paciente
from .forms import PacienteForm # Importação correta!

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    context = {'pacientes': pacientes}
    return render(request, 'pacientes/lista_pacientes.html', context)

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()

    context = {
        'form': form,
        'is_cadastro': True
    }
    return render(request, 'pacientes/cadastro_paciente.html', context)

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente atualizado com sucesso!')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)

    context = {
        'form': form,
        'is_cadastro': False
    }
    return render(request, 'pacientes/cadastro_paciente.html', context)

def excluir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('lista_pacientes')

    context = {
        'paciente': paciente
    }
    return render(request, 'pacientes/confirma_exclusao.html', context)