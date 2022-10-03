from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):

    def __init__(self, nome=None, cpf=None, saldo=None):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def imprimirDados(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nSaldo: {self.saldo}'

    @abstractmethod
    def cadastrar():
        pass

    @abstractmethod
    def depositar():
        pass

 