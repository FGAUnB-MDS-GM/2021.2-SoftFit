from ..models import AvaliacaoFisica

def cadastrar_aval(avaliacao):
    return AvaliacaoFisica.objects.create(peso=avaliacao.peso,
                                        altura=avaliacao.altura, 
                                        imc=avaliacao.peso/(avaliacao.altura*avaliacao.altura), 
                                        braco_d=avaliacao.braco_d, 
                                        perna_e=avaliacao.perna_e, 
                                        cintura=avaliacao.cintura, 
                                        comentario_af=avaliacao.comentario_af)

def mostrar_avaliacao(id):
    return AvaliacaoFisica.objects.get(id=id)

def editar_avaliacao(avaliacao, avaliacao_nova):
    avaliacao.peso = avaliacao_nova.peso
    avaliacao.altura = avaliacao_nova.altura
    avaliacao.imc = avaliacao_nova.peso/(avaliacao_nova.altura*avaliacao_nova.altura)
    avaliacao.braco_d = avaliacao_nova.braco_d
    avaliacao.perna_e = avaliacao_nova.perna_e
    avaliacao.cintura = avaliacao_nova.cintura
    avaliacao.comentario_af = avaliacao_nova.comentario_af
    avaliacao.save(force_update=True)
    return avaliacao

def remover_avaliacao(avaliacao):
    avaliacao.delete()