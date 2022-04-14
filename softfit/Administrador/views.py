from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroAluno, CadastroAvaliacao, CadastroProfessor
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .services import avaliacao_service, aluno_service, prof_service, estadof_service, objetivo_service
from .models import Aluno, Professor, EstadoFinanceiro, Objetivo
from .entidades import aluno, avaliacao, professor, estadof, objetivod

def index(request):
    alunos = Aluno.objects.all()
    profs = Professor.objects.all()
    return render(request, 'Administrador/inicial.html', {'alunos': alunos, 'profs': profs})

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

                estadof_novo = estadof.EstadoFinanceiro(condicao="Em Dia")
                estadof_db = estadof_service.cadastrar_estadof(estadof_novo)

                objetivo_novo = objetivod.Objetivo(opcao="A Selecionar", comentario="Nenhum, por enquanto")
                objetivo_db = objetivo_service.cadastrar_objetivo(objetivo_novo)

                aluno_novo = aluno.Aluno(idu=idu, nome=nome, email=email, avaliacao=avaliacao_db, estadof=estadof_db, frequencia=0, objetivo=objetivo_db)
                aluno_db = aluno_service.cadastrar_aluno(aluno_novo)

                senha = aluno_service.gera_senha()

                user = User.objects.create_user(username=email, email=email, password=senha)

                user.save()

                corpo_email = "Aluno, sua senha provisória de acesso é: " + senha

                send_mail('Senha de Acesso - SoftFit', corpo_email, 'softfit123@gmail.com', [email], fail_silently=False)

                return redirect('/administrador/')
    else:
        form_aluno = CadastroAluno()
        form_aval = CadastroAvaliacao()
    return render(request, 'administrador/cadastroaluno.html', {'form_aluno': form_aluno, 'form_aval': form_aval})

def editaAluno(request, id):
    aluno_editar = aluno_service.mostrar_aluno(id)
    form_aluno = CadastroAluno(request.POST or None, instance=aluno_editar)
    avaliacao_editar = avaliacao_service.mostrar_avaliacao(aluno_editar.avaliacao.id)
    form_aval = CadastroAvaliacao(request.POST or None, instance=avaliacao_editar)
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
            avaliacao_edit = avaliacao_service.editar_avaliacao(avaliacao_editar, avaliacao_novo)

            aluno_novo = aluno.Aluno(idu=idu, nome=nome, email=email, avaliacao=avaliacao_edit, frequencia=aluno_editar.frequencia, estadof=aluno_editar.estadof, objetivo=aluno_editar.objetivo)
            aluno_service.editar_aluno(aluno_editar, aluno_novo)
            return redirect('/administrador/')
    return render(request, 'administrador/cadastroaluno.html', {'form_aluno': form_aluno, 'form_aval': form_aval})

def mostraAluno(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    return render(request, 'administrador/mostraaluno.html', {'aluno': aluno})

def removeAluno(request, id):
    aluno = aluno_service.mostrar_aluno(id)
    avaliacao = avaliacao_service.mostrar_avaliacao(aluno.avaliacao.id)
    estadof = estadof_service.mostrar_estadof(aluno.estadof.id)
    objetivo = objetivo_service.mostrar_objetivo(aluno.objetivo.id)
    if request.method == "POST":
        aluno_service.remover_aluno(aluno)
        avaliacao_service.remover_avaliacao(avaliacao)
        estadof_service.remover_estadof(estadof)
        objetivo_service.remover_objetivo(objetivo)
        return redirect('/administrador/')
    return render(request, 'administrador/confirmarexclusao.html', {'usuario': aluno})

def cadastroProfessor(request):
    if request.method == "POST":
        form_prof = CadastroProfessor(request.POST)
        if form_prof.is_valid():
            idu = form_prof.cleaned_data["idu"]
            nome = form_prof.cleaned_data["nome"]
            email = form_prof.cleaned_data["email"]

            segunda_manha = form_prof.cleaned_data["segunda_manha"]
            segunda_tarde = form_prof.cleaned_data["segunda_tarde"]
            segunda_noite = form_prof.cleaned_data["segunda_noite"]

            terca_manha = form_prof.cleaned_data["terca_manha"]
            terca_tarde = form_prof.cleaned_data["terca_tarde"]
            terca_noite = form_prof.cleaned_data["terca_noite"]

            quarta_manha = form_prof.cleaned_data["quarta_manha"]
            quarta_tarde = form_prof.cleaned_data["quarta_tarde"]
            quarta_noite = form_prof.cleaned_data["quarta_noite"]

            quinta_manha = form_prof.cleaned_data["quinta_manha"]
            quinta_tarde = form_prof.cleaned_data["quinta_tarde"]
            quinta_noite = form_prof.cleaned_data["quinta_noite"]

            sexta_manha = form_prof.cleaned_data["sexta_manha"]
            sexta_tarde = form_prof.cleaned_data["sexta_tarde"]
            sexta_noite = form_prof.cleaned_data["sexta_noite"]

            sabado_manha = form_prof.cleaned_data["sabado_manha"]
            sabado_tarde = form_prof.cleaned_data["sabado_tarde"]

            domingo_manha = form_prof.cleaned_data["domingo_manha"]

            prof_novo = professor.Professor(idu=idu, nome=nome, email=email, 
                                    segunda_manha=segunda_manha, segunda_tarde=segunda_tarde, segunda_noite=segunda_noite, 
                                    terca_manha=terca_manha, terca_tarde=terca_tarde, terca_noite=terca_noite, 
                                    quarta_manha=quarta_manha, quarta_tarde=quarta_tarde, quarta_noite=quarta_noite, 
                                    quinta_manha=quinta_manha, quinta_tarde=quinta_tarde, quinta_noite=quinta_noite, 
                                    sexta_manha=sexta_manha, sexta_tarde=sexta_tarde, sexta_noite=sexta_noite, 
                                    sabado_manha=sabado_manha, sabado_tarde=sabado_tarde, 
                                    domingo_manha=domingo_manha)
            prof_db = prof_service.cadastrar_professor(prof_novo)

            senha = aluno_service.gera_senha()

            user = User.objects.create_user(username=email, email=email, password=senha)

            user.save()

            corpo_email = "Professor, sua senha provisória de acesso é: " + senha

            send_mail('Senha de Acesso - SoftFit', corpo_email, 'softfit123@gmail.com', [email], fail_silently=False)

            return redirect('/administrador/')
    else:
        form_prof = CadastroProfessor()
    return render(request, 'administrador/cadastroprofessor.html', {'form_prof': form_prof})

def removeProfessor(request, id):
    prof = prof_service.mostrar_professor(id)
    if request.method == "POST":
        prof_service.remover_professor(prof)
        return redirect('/administrador/')
    return render(request, 'administrador/confirmarexclusao.html', {'usuario': prof})

def editaProfessor(request, id):
    prof_editar = prof_service.mostrar_professor(id)
    form_prof = CadastroProfessor(request.POST or None, instance=prof_editar)
    if form_prof.is_valid():
        idu = form_prof.cleaned_data["idu"]
        nome = form_prof.cleaned_data["nome"]
        email = form_prof.cleaned_data["email"]

        segunda_manha = form_prof.cleaned_data["segunda_manha"]
        segunda_tarde = form_prof.cleaned_data["segunda_tarde"]
        segunda_noite = form_prof.cleaned_data["segunda_noite"]

        terca_manha = form_prof.cleaned_data["terca_manha"]
        terca_tarde = form_prof.cleaned_data["terca_tarde"]
        terca_noite = form_prof.cleaned_data["terca_noite"]

        quarta_manha = form_prof.cleaned_data["quarta_manha"]
        quarta_tarde = form_prof.cleaned_data["quarta_tarde"]
        quarta_noite = form_prof.cleaned_data["quarta_noite"]

        quinta_manha = form_prof.cleaned_data["quinta_manha"]
        quinta_tarde = form_prof.cleaned_data["quinta_tarde"]
        quinta_noite = form_prof.cleaned_data["quinta_noite"]

        sexta_manha = form_prof.cleaned_data["sexta_manha"]
        sexta_tarde = form_prof.cleaned_data["sexta_tarde"]
        sexta_noite = form_prof.cleaned_data["sexta_noite"]

        sabado_manha = form_prof.cleaned_data["sabado_manha"]
        sabado_tarde = form_prof.cleaned_data["sabado_tarde"]

        domingo_manha = form_prof.cleaned_data["domingo_manha"]

        prof_novo = professor.Professor(idu=idu, nome=nome, email=email, 
                                    segunda_manha=segunda_manha, segunda_tarde=segunda_tarde, segunda_noite=segunda_noite, 
                                    terca_manha=terca_manha, terca_tarde=terca_tarde, terca_noite=terca_noite, 
                                    quarta_manha=quarta_manha, quarta_tarde=quarta_tarde, quarta_noite=quarta_noite, 
                                    quinta_manha=quinta_manha, quinta_tarde=quinta_tarde, quinta_noite=quinta_noite, 
                                    sexta_manha=sexta_manha, sexta_tarde=sexta_tarde, sexta_noite=sexta_noite, 
                                    sabado_manha=sabado_manha, sabado_tarde=sabado_tarde, 
                                    domingo_manha=domingo_manha)

        prof_service.editar_professor(prof_editar, prof_novo)
        return redirect('/administrador/')
    return render(request, 'administrador/cadastroprofessor.html', {'form_prof': form_prof})