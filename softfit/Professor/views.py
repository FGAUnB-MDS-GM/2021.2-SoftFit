from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Administrador.services import prof_service
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from Administrador.services import prof_service, aluno_service, avaliacao_service, objetivo_service
from Administrador.models import Aluno, Professor

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
    return render(request, 'Professor/criartreino.html')
