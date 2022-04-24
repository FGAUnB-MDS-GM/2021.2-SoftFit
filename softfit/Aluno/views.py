from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from Administrador.services import aluno_service, avaliacao_service, objetivo_service
from Administrador.forms import CadastroObjetivo
from Administrador.entidades import objetivod
from django.contrib.auth.decorators import login_required
from datetime import date
import homepage

# Create your views here.
@login_required(login_url='/aluno/loginAluno/')
def inicial(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    nao_frequencia = aluno.data_frequencia == date.today()
    print(nao_frequencia)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    objetivo = objetivo_service.mostrar_objetivo(aluno.objetivo.id)
    return render(request, 'Aluno/inicial.html', {'aluno': aluno, 'avaliacao': avaliacao, 'objetivo': objetivo, 'nao_frequencia': nao_frequencia})

@login_required(login_url='/aluno/loginAluno/')
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
        
        return HttpResponseRedirect(reverse('aluno:inicial', kwargs={'id':id}))
    return render(request, 'aluno/objetivo.html', {'form_objetivo': form_objetivo})

def frequencia(request, id):
    aluno_service.att_frequencia(id)
    return HttpResponseRedirect(reverse('aluno:inicial', kwargs={'id':id}))

def loginAluno(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            id_aluno = aluno_service.encontra_id(email)
            login(request, user)
            return HttpResponseRedirect(reverse('aluno:inicial', kwargs={'id':id_aluno}))
        else:
            return render(request, "Aluno/login.html", {
                "message": "Aluno não encontrado!"
            })
    else:
        return render(request, "Aluno/login.html")

def logout_view(request):
    logout(request)
    return render(request, "homepage/index.html", {
        "message": "Log out realizado!"
    })