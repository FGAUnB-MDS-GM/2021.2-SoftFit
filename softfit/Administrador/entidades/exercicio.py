class Exercicio():
    def __init__(self, serie, qntd_serie, repeticao, carga, descanso, comentario_ex, treino_ex, aluno_ex):
    self.__serie = serie
    self.__qntd_serie = qntd_serie
    self.__repeticao = repeticao
    self.__carga = carga
    self.__descanso = descanso
    self.__comentario_ex = comentario_ex
    self.__treino_ex = treino_ex
    self.__aluno_ex = aluno_ex

    @property
    def serie(self):
        return self.__serie
    
    @serie.setter
    def serie(self, serie):
        self.__serie = serie

    @property
    def qntd_serie(self):
        return self.__qntd_serie
    
    @qntd_serie.setter
    def qntd_serie(self, qntd_serie):
        self.__qntd_serie = qntd_serie

    @property
    def repeticao(self):
        return self.__repeticao
    
    @repeticao.setter
    def repeticao(self, repeticao):
        self.__repeticao = repeticao

    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def descanso(self):
        return self.__descanso
    
    @descanso.setter
    def descanso(self, descanso):
        self.__descanso = descanso

    @property
    def comentario_ex(self):
        return self.__comentario_ex
    
    @comentario_ex.setter
    def comentario_ex(self, comentario_ex):
        self.__comentario_ex = comentario_ex

    @property
    def treino_ex(self):
        return self.__treino_ex
    
    @treino_ex.setter
    def treino_ex(self, treino_ex):
        self.__treino_ex = treino_ex

    @property
    def aluno_ex(self):
        return self.__aluno_ex
    
    @aluno_ex.setter
    def aluno_ex(self, aluno_ex):
        self.__aluno_ex = aluno_ex