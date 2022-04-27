from django.test import TestCase
from Administrador.models import Professor, Aluno, Objetivo, AvaliacaoFisica, EstadoFinanceiro, Treino, Exercicio
from Administrador.services import aluno_service, objetivo_service, prof_service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your tests here.

# H24 - Login Professor
class ProfessorTestCase(TestCase):
    def setUp(self):
        # A senha inicial é aquela enviada por e-mail após o cadastro feito pelo administrador.
        User.objects.create_user(username="prof@prof.com", email="prof@prof.com", password="recebida_email")
    
        avaliacao = AvaliacaoFisica.objects.create(peso=10, altura=10, imc=0, braco_d=40, perna_e=80, cintura=120, 
                                                    comentario_af="nenhum")
        objetivo = Objetivo.objects.create(opcao="A Selecionar", comentario="Nenhum, por enquanto")
        estadof = EstadoFinanceiro.objects.create(condicao="Em Dia")
        aluno = Aluno.objects.create(nome="Victor", email="victor.pessoal1203@gmail.com", 
                                avaliacao=avaliacao, frequencia=0, objetivo=objetivo, estadof=estadof)

        # Na criação do treino, o professor deve selecionar um dos treinos/tipos de exercício pré-cadastrados.
        treino = Treino.objects.create(descricao="Puxada")
        # Para cada exercício selecionado, o professor deverá adicionar a quantidade de séries, quantidade por séries, carga e tempo de descanso (esses números devem ser maiores que 0). (Os formulários avaliam os valores)
        # Um comentário adicional pode ser feito.
        Exercicio.objects.create(serie=3, qntd_serie=12, carga=40, descanso=60, comentario_ex="Fazer todo dia", treino_ex=treino, aluno_ex=aluno)

    def test_login_prof(self):
        # O login deve ser realizado com e-mail cadastrado e senha.
        user = authenticate(username="prof@prof.com", password="recebida_email")
        # Caso um usuário com e-mail e senha preenchidos não forem encontrados, a página de login deverá ser atualizada com a mensagem "Professor não encontrado!".
        self.assertNotEqual(user, None, msg="Professor não encontrado!")

    # H13 - Visualizar Obj. e Aval.
    def test_obj_aval(self):
        victor = Aluno.objects.get(nome="Victor")
        # As medidas a serem dispostas devem estar nos sistemas de cm ou kg.
        peso = str(victor.avaliacao.peso) + "cm"
        self.assertEqual(peso, "10.00cm")
        # Além de ver o objetivo, o professor também deve ser capaz de ver o comentário que um aluno pode colocar acerca dele (objetivo).
        self.assertEqual(victor.objetivo.opcao, "A Selecionar")
        self.assertEqual(victor.objetivo.comentario, "Nenhum, por enquanto")

    def test_treino(self):
        exercicio = Exercicio.objects.get(serie=3)
        self.assertNotEqual(exercicio, None)