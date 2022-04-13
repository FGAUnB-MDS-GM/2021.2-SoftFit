class EstadoFinanceiro():
    def __init__(self, condicao):
        self.__condicao = condicao
    
    @property
    def condicao(self):
        return self.__condicao

    @condicao.setter
    def condicao(self, condicao):
        self.__condicao = condicao