from ..models import Professor

def cadastrar_professor(prof):
    return Professor.objects.create(idu=prof.idu, nome=prof.nome, email=prof.email, 
                                    rotina=0)

def mostrar_professor(id):
    return Professor.objects.get(id=id)

def editar_professor(prof, prof_novo):
    prof.idu = prof_novo.idu
    prof.nome = prof_novo.nome
    prof.email = prof_novo.email
    prof.rotina = prof_novo.rotina
    prof.save(force_update=True)

def remover_professor(prof):
    prof.delete()