from django.db import models

# Create your models here.

class Usuario(models.Model):
    idu = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        abstract = True

class AvaliacaoFisica(models.Model):
    peso = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5)
    altura = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5)
    imc = models.DecimalField(decimal_places=2, max_digits=5)
    braco_d = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5)
    perna_e = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5) 
    cintura = models.DecimalField(blank=False , null = False,decimal_places=2, max_digits=5)
    comentario_af = models.CharField(max_length=500)

class EstadoFinanceiro(models.Model):

    STATUS = (
        ('dia', 'Em Dia'),
        ('ina', 'Inadimplente'),
    )

    d_pagamento = models.DateField()
    condicao = models.CharField(
        max_length=3,
        choices=STATUS,
    )

class Objetivo(models.Model):

    OBJS = (
        ('musculo', 'Ganhar massa muscular'),
        ('emagrecer', 'Emagrecer'),
        ('resistencia', 'Ganhar resistência'),
    )

    opcao = models.CharField(
        max_length=11,
        choices=OBJS,
    )

    comentario = models.CharField(max_length=500)

class Aluno(Usuario): 
    avaliacao = models.ForeignKey(AvaliacaoFisica, on_delete=models.CASCADE)
    estadoFin = models.ForeignKey(EstadoFinanceiro, on_delete=models.CASCADE, null=True)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE, null=True)
    frequencia = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome