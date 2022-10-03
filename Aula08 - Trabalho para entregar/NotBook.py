from Computador import Computador


class NotBook(Computador):
    def __init__(self, modelo=None, cor=None, valor=None, tempoDeBateria=None):
        super().__init__(modelo, cor, valor)
        self.__tempoDeBateria = tempoDeBateria
        print('NotBook Construido')

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__ = valor

    def getInformacoes(self):
        return super().getInformacoes() + f'\nTempo de bateria: {self.__tempoDeBateria} horas'

    def cadastrar(self, modelo, cor, valor, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.__tempoDeBateria = tempoDeBateria
