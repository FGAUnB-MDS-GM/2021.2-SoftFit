from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroAluno, CadastroAvaliacao

from .services import avaliacao_service, aluno_service
from .models import Aluno
from .entidades import aluno, avaliacao

def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'Administrador/inicial.html', {'alunos': alunos})

def cadastroAluno(request):
    if request.method == "POST":
        form_aluno = CadastroAluno(request.POST)
        form_aval = CadastroAvaliacao(request.POST)
        if form_aluno.is_valid():
            idu = form_aluno.cleaned_data["idu"]
            nome = form_aluno.cleaned_data["nome"]
            email = form_aluno.cleaned_data["email"]
            if form_aval.is_valid():
                peso = form_aval.cleaned_data["peso"]
                altura = form_aval.cleaned_data["altura"]
                imc = peso/(altura*altura)
                braco_d = form_aval.cleaned_data["braco_d"]
                perna_e = form_aval.cleaned_data["perna_e"]
                cintura = form_aval.cleaned_data["cintura"]
                comentario_af = form_aval.cleaned_data["comentario_af"]
                avaliacao_novo = avaliacao.AvaliacaoFisica(peso=peso, altura=altura, imc=imc, braco_d=braco_d, perna_e=perna_e, cintura=cintura, comentario_af=comentario_af)
                avaliacao_db = avaliacao_service.cadastrar_aval(avaliacao_novo)
                if avaliacao_db.id > 0:
                    aluno_novo = aluno.Aluno(idu=idu, nome=nome, email=email, avaliacao=avaliacao_db)
                    aluno_db = aluno_service.cadastrar_aluno(aluno_novo)
                    if aluno_db.id > 0:
                        return redirect('/administrador/')
                    else:
                        print("erro ao gravar aluno")
                else:
                    print("erro ao gravar avaliacao")
    else:
        form_aluno = CadastroAluno()
        form_aval = CadastroAvaliacao()
    return render(request, 'administrador/cadastroaluno.html', {'form_aluno': form_aluno, 'form_aval': form_aval})