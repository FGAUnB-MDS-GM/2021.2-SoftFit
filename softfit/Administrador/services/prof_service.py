from ..models import Professor

def cadastrar_professor(prof):
    return Professor.objects.create(idu=prof.idu, nome=prof.nome, email=prof.email, 
                                    segunda_manha=prof.segunda_manha, segunda_tarde=prof.segunda_tarde, segunda_noite=prof.segunda_noite, 
                                    terca_manha=prof.terca_manha, terca_tarde=prof.terca_tarde, terca_noite=prof.terca_noite, 
                                    quarta_manha=prof.quarta_manha, quarta_tarde=prof.quarta_tarde, quarta_noite=prof.quarta_noite, 
                                    quinta_manha=prof.quinta_manha, quinta_tarde=prof.quinta_tarde, quinta_noite=prof.quarta_noite, 
                                    sexta_manha=prof.sexta_manha, sexta_tarde=prof.sexta_tarde, sexta_noite=prof.sexta_noite, 
                                    sabado_manha=prof.sabado_manha, sabado_tarde=prof.sabado_tarde, 
                                    domingo_manha=prof.domingo_manha)

def mostrar_professor(id):
    return Professor.objects.get(id=id)

def editar_professor(prof, prof_novo):
    prof.idu = prof_novo.idu
    prof.nome = prof_novo.nome
    prof.email = prof_novo.email

    prof.segunda_manha = prof_novo.segunda_manha
    prof.segunda_tarde = prof_novo.segunda_tarde
    prof.segunda_noite = prof_novo.segunda_noite

    prof.terca_manha = prof_novo.terca_manha
    prof.terca_tarde = prof_novo.terca_tarde
    prof.terca_noite = prof_novo.terca_noite

    prof.quarta_manha = prof_novo.quarta_manha
    prof.quarta_tarde = prof_novo.quarta_tarde
    prof.quarta_noite = prof_novo.quarta_noite

    prof.quinta_manha = prof_novo.quinta_manha
    prof.quinta_tarde = prof_novo.quinta_tarde
    prof.quinta_noite = prof_novo.quinta_noite

    prof.sexta_manha = prof_novo.sexta_manha
    prof.sexta_tarde = prof_novo.sexta_tarde
    prof.sexta_noite = prof_novo.sexta_noite

    prof.sabado_manha = prof_novo.sabado_manha
    prof.sabado_tarde = prof_novo.sabado_tarde

    prof.domingo_manha = prof_novo.domingo_manha

    prof.save(force_update=True)

def remover_professor(prof):
    prof.delete()