# clinica_odonto/dentistas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dentista
from .forms import DentistaForm

def lista_dentistas(request):
    dentistas = Dentista.objects.all()
    context = {'dentistas': dentistas}
    return render(request, 'dentistas/lista_dentistas.html', context)

def cadastrar_dentista(request):
    if request.method == 'POST':
        form = DentistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dentista cadastrado com sucesso!')
            return redirect('lista_dentistas')
    else:
        form = DentistaForm()

    context = {
        'form': form,
        'is_cadastro': True
    }
    return render(request, 'dentistas/cadastro_dentista.html', context)

def editar_dentista(request, pk):
    dentista = get_object_or_404(Dentista, pk=pk)
    if request.method == 'POST':
        form = DentistaForm(request.POST, instance=dentista)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dentista atualizado com sucesso!')
            return redirect('lista_dentistas')
    else:
        form = DentistaForm(instance=dentista)

    context = {
        'form': form,
        'is_cadastro': False
    }
    return render(request, 'dentistas/cadastro_dentista.html', context)

def excluir_dentista(request, pk):
    dentista = get_object_or_404(Dentista, pk=pk)
    if request.method == 'POST':
        dentista.delete()
        messages.success(request, 'Dentista excluído com sucesso!')
        return redirect('lista_dentistas')

    context = {'dentista': dentista}
    return render(request, 'dentistas/confirma_exclusao.html', context)