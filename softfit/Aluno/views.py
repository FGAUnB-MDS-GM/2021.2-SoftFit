from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
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
        
        return render(request, 'aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao, 'objetivo': objetivo})
    return render(request, 'aluno/objetivo.html', {'form_objetivo': form_objetivo})

def loginAluno(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            id_aluno = aluno_service.encontra_id(email)
            print(id_aluno)
            login(request, user)
            return render(request, "aluno/inicial.html")
        else:
            return render(request, "aluno/login.html", {
                "message": "Aluno não encontrado!"
            })
    else:
        return render(request, "aluno/login.html")