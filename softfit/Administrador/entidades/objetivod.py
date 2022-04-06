class Objetivo():
    def __init__(self, opcao, comentario):
        self.__opcao=opcao
        self.__comentario=comentario
    
    @property
    def opcao(self):
        return self.__opcao

    @opcao.setter
    def opcao(self, opcao):
        self.__opcao=opcao

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario=comentario