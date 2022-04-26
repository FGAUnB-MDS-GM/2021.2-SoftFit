from ..models import Exercicio, Treino

def cadastrar_exercicio(exercicio):
    return Exercicio.objects.create(serie=exercicio.serie, qntd_serie=exercicio.qntd_serie, carga=exercicio.carga, descanso=exercicio.descanso, comentario_ex=exercicio.comentario_ex, treino_ex=exercicio.treino_ex, aluno_ex=exercicio.aluno_ex)

def mostrar_exercicio(id):
    return Exercicio.objects.get(id=id)

def editar_exercicio(exercicio, exercicio_novo):
    exercicio.serie=exercicio_novo.serie
    exercicio.qntd_serie=exercicio_novo.qntd_serie
    exercicio.carga=exercicio_novo.carga
    exercicio.descanso=exercicio_novo.descanso
    exercicio.comentario_ex=exercicio_novo.comentario_ex
    exercicio.treino_ex=exercicio_novo.treino_ex
    exercicio.aluno_ex=exercicio_novo.aluno_ex

def remover_exercicio(exercicio):
    exercicio.delete()

def mostrar_treino(id):
    return Treino.objects.get(id=id)

def mostrar_exercicio_aluno(id):
    return Exercicio.objects.filter(aluno_ex_id=id)

def remover_exercicio_aluno(id):
    exercicios = Exercicio.objects.filter(aluno_ex_id=id)
    for exercicio in exercicios:
        exercicio.delete()