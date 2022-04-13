class AvaliacaoFisica():
    def __init__(self, peso, altura, imc, braco_d, perna_e, cintura, comentario_af):
        self.__peso = peso
        self.__altura = altura
        self.__imc = imc
        self.__braco_d = braco_d
        self.__perna_e = perna_e
        self.__cintura = cintura
        self.__comentario_af= comentario_af

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def imc(self):
        return self.__imc

    @imc.setter
    def imc(self, imc):
        self.__imc = imc

    @property
    def braco_d(self):
        return self.__braco_d

    @braco_d.setter
    def braco_d(self, braco_d):
        self.__braco_d = braco_d

    @property
    def perna_e(self):
        return self.__perna_e

    @perna_e.setter
    def perna_e(self, perna_e):
        self.__perna_e = perna_e

    @property
    def cintura(self):
        return self.__cintura

    @cintura.setter
    def cintura(self, cintura):
        self.__cintura = cintura

    @property
    def comentario_af(self):
        return self.__comentario_af

    @comentario_af.setter
    def comentario_af(self, comentario_af):
        self.__comentario_af = comentario_af