from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from Administrador.services import aluno_service, avaliacao_service, objetivo_service
from Administrador.forms import CadastroObjetivo
from Administrador.entidades import objetivod

# Create your views here.
def inicial(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    objetivo = objetivo_service.mostrar_objetivo(aluno.objetivo.id)
    return render(request, 'Aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao, 'objetivo': objetivo})

def objetivo(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    obj_editar = objetivo_service.mostrar_objetivo(aluno.objetivo.id)
    form_objetivo = CadastroObjetivo(request.POST or None, instance=obj_editar)
    if form_objetivo.is_valid():
        opcao = form_objetivo.cleaned_data["opcao"]
        comentario = form_objetivo.cleaned_data["comentario"]

        obj_novo = objetivod.Objetivo(opcao=opcao, comentario=comentario)
        objetivo = objetivo_service.editar_objetivo(obj_editar, obj_novo)
        
        return render(request, 'Aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao, 'objetivo': objetivo})
    return render(request, 'aluno/objetivo.html', {'form_objetivo': form_objetivo})