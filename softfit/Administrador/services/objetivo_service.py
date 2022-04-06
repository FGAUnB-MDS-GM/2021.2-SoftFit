from ..models import Objetivo

def cadastrar_objetivo(objetivo):
    return Objetivo.objects.create(opcao=objetivo.opcao,
                                comentario=objetivo.comentario)

def mostrar_objetivo(id):
    return Objetivo.objects.get(id=id)

def editar_objetivo(objetivo, objetivo_novo):
    objetivo.opcao = objetivo_novo.opcao
    objetivo.comentario = objetivo_novo.comentario
    objetivo.save(force_update=True)
    return objetivo

def remover_objetivo(objetivo):
    objetivo.delete()