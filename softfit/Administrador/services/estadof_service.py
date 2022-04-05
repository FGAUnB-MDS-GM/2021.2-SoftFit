from ..models import EstadoFinanceiro

def cadastrar_estadof(estadof):
    return EstadoFinanceiro.objects.create(condicao=estadof.condicao)

def mostrar_estadof(id):
    return EstadoFinanceiro.objects.get(id=id)

def editar_estadof(estadof, estadof_novo):
    estadof.condicao = estadof_novo.condicao
    estadof.save(force_update=True)
    return estadof

def remover_estadof(estadof):
    estadof.delete()