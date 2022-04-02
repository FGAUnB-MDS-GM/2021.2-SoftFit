from ..models import Aluno

def cadastrar_aluno(aluno):
    return Aluno.objects.create(idu=aluno.idu, nome=aluno.nome, email=aluno.email, 
                        avaliacao=aluno.avaliacao, frequencia=0)