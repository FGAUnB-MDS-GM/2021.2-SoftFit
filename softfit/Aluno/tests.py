from django.test import TestCase
from Administrador.models import Aluno, Objetivo, AvaliacaoFisica, EstadoFinanceiro, Treino, Exercicio
from Administrador.services import aluno_service, objetivo_service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your tests here.

# H22 - Login Aluno
class AlunoTestCase(TestCase):
    def setUp(self):
        avaliacao = AvaliacaoFisica.objects.create(peso=10, altura=10, imc=0, braco_d=40, perna_e=80, cintura=120, 
                                                    comentario_af="nenhum")
        objetivo = Objetivo.objects.create(opcao="A Selecionar", comentario="Nenhum, por enquanto")
        # H10 - O aluno poderá adicionar comentários acerca de seu objetivo.
        # O aluno terá algumas opções para selecionar, como: ganho de massa muscular, emagrecer ou ganhar resistência.
        # H11 - O aluno poderá alterar sua opção de objetivo ou comentário.
        Objetivo.objects.create(opcao="Emagrecer", comentario="Gostaria de perder 10kg em 3 meses")
        estadof = EstadoFinanceiro.objects.create(condicao="Em Dia")
        victor = Aluno.objects.create(nome="Victor", email="victor.pessoal1203@gmail.com", 
                                avaliacao=avaliacao, frequencia=0, objetivo=objetivo, estadof=estadof)
        # H22 - A senha inicial é aquela enviada por e-mail após o cadastro feito pelo administrador.
        User.objects.create_user(username="aluno@aluno.com", email="aluno@aluno.com", password="recebida_email")

        # H15 - Consultar Treinos
        treino = Treino.objects.create(descricao="Puxada")
        Exercicio.objects.create(serie=3, qntd_serie=12, carga=40, descanso=60, treino_ex=treino, aluno_ex=victor)


    def test_login_aluno(self):
        # O login deve ser realizado com e-mail cadastrado e senha.
        user = authenticate(username="aluno@aluno.com", password="recebida_email")
        # Caso um usuário com e-mail e senha preenchidos não forem encontrados, a página de login deverá ser atualizada com a mensagem "Administrador não encontrado!".
        self.assertNotEqual(user, None, msg="Aluno não encontrado!")

    # H10 - Cadastrar Objetivo
    def test_objetivo(self):
        victor = Aluno.objects.get(nome="Victor")
        # A princípio, o aluno terá seu objetivo a selecionar e com um comentário padrão.
        self.assertEqual(victor.objetivo.opcao, "A Selecionar")
        self.assertEqual(victor.objetivo.comentario, "Nenhum, por enquanto")
        # H11 - Alterar Objetivos
        objetivo = Objetivo.objects.get(opcao="A Selecionar")
        objetivo_novo = Objetivo.objects.get(opcao="Emagrecer")
        novo = objetivo_service.editar_objetivo(objetivo, objetivo_novo)
        self.assertEqual(novo.opcao, "Emagrecer")

    # H15 - Consultar Treinos
    def test_treino(self):
        # Para cada exercício, são listadas seus campos: séries, quantidades por série, carga (em kg), descanso (em seg) e o comentário.
        exercicio = Exercicio.objects.get(serie=3)
        self.assertEqual(exercicio.serie, 3)
        self.assertEqual(exercicio.qntd_serie, 12)
        carga = str(exercicio.carga) + "kg"
        self.assertEqual(carga, "40.0kg")
        descanso = str(exercicio.descanso) + "seg"
        self.assertEqual(descanso, "60.0seg")
        # Caso o comentário seja vazio, deverá aparecer: "Comentário: None".
        self.assertEqual(exercicio.comentario_ex, None)