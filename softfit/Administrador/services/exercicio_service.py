from ..models import Exercicio

def cadastrar_exercicio(exercicio):
    return Exercicio.objects.create(serie=exercicio.serie, qntd_serie=exercicio.qntd_serie, repeticao=exercicio.repeticao, carga=exercicio.carga, descanso=exercicio.descanso, comentario_ex=exercicio.comentario_ex, treino_ex=exercicio.treino_ex, aluno_ex=exercicio.aluno_ex)

def editar_exercicio(exercicio, exercicio_novo):
    exercicio.serie=exercicio_novo.serie
    exercicio.qntd_serie=exercicio_novo.qntd_serie
    exercicio.repeticao=exercicio_novo.repeticao
    exercicio.carga=exercicio_novo.carga
    exercicio.descanso=exercicio_novo.descanso
    exercicio.comentario_ex=exercicio_novo.comentario_ex
    exercicio.treino_ex=exercicio_novo.treino_ex
    exercicio.aluno_ex=exercicio_novo.aluno_ex

def remover_objetivo(exercicio):
    exercicio.delete()