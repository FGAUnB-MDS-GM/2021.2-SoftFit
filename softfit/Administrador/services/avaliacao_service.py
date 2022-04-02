from ..models import AvaliacaoFisica

def cadastrar_aval(avaliacao):
    return AvaliacaoFisica.objects.create(peso=avaliacao.peso,
                                        altura=avaliacao.altura, 
                                        imc=avaliacao.peso/(avaliacao.altura*avaliacao.altura), 
                                        braco_d=avaliacao.braco_d, 
                                        perna_e=avaliacao.perna_e, 
                                        cintura=avaliacao.cintura, 
                                        comentario_af=avaliacao.comentario_af)