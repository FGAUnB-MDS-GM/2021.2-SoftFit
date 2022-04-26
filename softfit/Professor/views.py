from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Administrador.services import prof_service
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from Administrador.services import prof_service, aluno_service, avaliacao_service, objetivo_service, exercicio_service
from Administrador.models import Aluno, Professor, Exercicio, Treino
from Administrador.entidades import exer

from .forms import CadastroTreino, CadastroExercicio

def prof_check(user):
    for prof in Professor.objects.all():
        if user.username == prof.email:
            return True
    return False

def loginProf(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            id_prof = prof_service.encontra_id(email)
            login(request, user)
            return HttpResponseRedirect(reverse('professor:inicial', kwargs={'id':id_prof}))
        else:
            return render(request, "Professor/login.html", {
                "message": "Professor não encontrado!"
            })
    else:
        return render(request, "Professor/login.html")

def logout_view(request):
    logout(request)
    
    return render(request, "homepage/index.html", {
        "message": "Log out realizado!"
    })

# Create your views here.
@user_passes_test(prof_check, login_url='/professor/loginProf/')
def inicial(request, id):
    prof = prof_service.mostrar_professor(id)
    alunos = Aluno.objects.all()
    return render(request, 'Professor/inicial.html', {'prof': prof, 'alunos': alunos})

@user_passes_test(prof_check, login_url='/professor/loginProf/')
def verAluno(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    objetivo = objetivo_service.mostrar_objetivo(aluno.objetivo.id)
    return render(request, 'Professor/veraluno.html', {'aluno': aluno, 'avaliacao': avaliacao, 'objetivo': objetivo})

@user_passes_test(prof_check, login_url='/professor/loginProf/')
def criarTreino(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    treinos = Treino.objects.all()
    exercicios = exercicio_service.mostrar_exercicio_aluno(id)
    if request.method == "POST":
        form_exer = CadastroExercicio(request.POST)
        form_treino = CadastroTreino(request.POST)
        if form_treino.is_valid():
            treino = form_treino.cleaned_data["treino"]
            treino_ex = exercicio_service.mostrar_treino(treino)
            if form_exer.is_valid():
                serie = form_exer.cleaned_data["serie"]
                qntd_serie = form_exer.cleaned_data["qntd_serie"]
                carga = form_exer.cleaned_data["carga"]
                descanso = form_exer.cleaned_data["descanso"]
                comentario_ex = form_exer.cleaned_data["comentario_ex"]

                exercicio_novo = exer.Exercicio(serie=serie, qntd_serie=qntd_serie, carga=carga, descanso=descanso, comentario_ex=comentario_ex, treino_ex=treino_ex, aluno_ex=aluno)
                exercicio_db = exercicio_service.cadastrar_exercicio(exercicio_novo)
    
                return render(request, 'Professor/criartreino.html', {'aluno': aluno, 'treinos': treinos, 'form_exer': form_exer, 'form_treino': form_treino, 'exercicios': exercicios})
    else:
        form_exer = CadastroExercicio()
        form_treino = CadastroTreino()
    return render(request, 'Professor/criartreino.html', {'aluno': aluno, 'treinos': treinos, 'form_exer': form_exer, 'form_treino': form_treino, 'exercicios': exercicios})

@user_passes_test(prof_check, login_url='/professor/loginProf/')
def removerTreino(request, id, id_aluno):
    exercicio = exercicio_service.mostrar_exercicio(id)
    exercicio_service.remover_exercicio(exercicio)
    return HttpResponseRedirect(reverse('professor:criarTreino', kwargs={'id': id_aluno}))