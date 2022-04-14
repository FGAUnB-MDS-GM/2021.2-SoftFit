from ..models import Aluno
import string
from random import choice

def cadastrar_aluno(aluno):
    return Aluno.objects.create(idu=aluno.idu, nome=aluno.nome, email=aluno.email, 
                        avaliacao=aluno.avaliacao, frequencia=0, estadof= aluno.estadof, objetivo=aluno.objetivo)

def mostrar_aluno(id):
    return Aluno.objects.get(id=id)

def editar_aluno(aluno, aluno_novo):
    aluno.idu = aluno_novo.idu
    aluno.nome = aluno_novo.nome
    aluno.email = aluno_novo.email
    aluno.avaliacao = aluno_novo.avaliacao
    aluno.estadof = aluno_novo.estadof
    aluno.frequencia = aluno_novo.frequencia
    aluno.objetivo = aluno_novo.objetivo
    aluno.save(force_update=True)

def remover_aluno(aluno):
    aluno.delete()

def gera_senha():
    tamanho = 8
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    
    return senha

def encontra_id(email):
    for aluno in Aluno.objects.all():
        if email == aluno.email:
            return aluno.id