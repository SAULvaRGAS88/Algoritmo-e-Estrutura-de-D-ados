from abc import ABCMeta, abstractmethod

class Veiculo(metaclass=ABCMeta):
    
    def __init__(self, modelo= None, ano=None):
        self.__modelo=modelo
        self._ano=ano
        print('Veiculo construído')

    def imprimir(self):
        print("Modelo: ", self.__modelo)
        print("Ano: ", self._ano)


    @abstractmethod
    def imprimirEspecifico(self):
        pass


    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__ = valor

    @property
    def ano(self):
        return self.ano

    @modelo.setter
    def ano(self, valor):
        self._ano = valor    