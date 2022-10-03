from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self,  nome=None, cpf=None, saldo=None, manutencao=None):
        super().__init__(nome, cpf, saldo)
        self.manutencao = manutencao
        print('Conta Criada')

    def imprimirDados(self):
        return super().imprimirDados() + f'\nDesconto de manutenção de conta: {self.manutencao}'

    def cadastrar(self, nome, cpf, saldo, manutencao):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.manutencao = manutencao

    def depositar(self):
        return self.depositar()
