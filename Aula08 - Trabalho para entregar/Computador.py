from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):

    def __init__(self, modelo= None, cor= None, valor= None):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor

    def getInformacoes(self):
        return f'Modelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.valor}'
        
    @abstractmethod
    def cadastrar():
        pass