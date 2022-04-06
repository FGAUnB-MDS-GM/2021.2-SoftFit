from django.shortcuts import render
from django.http import HttpResponse
from Administrador.services import aluno_service, avaliacao_service

# Create your views here.
def index(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    return render(request, 'Aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao})

def cadastroObjetivo(request):
    return render(request, 'Aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao})