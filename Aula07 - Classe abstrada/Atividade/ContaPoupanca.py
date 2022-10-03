from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome=None, cpf=None, saldo=None, rendimento=None):
        super().__init__(nome, cpf, saldo)
        self.rendimento = rendimento
        print('Conta Criada')

    def imprimirDados(self):
        return super().imprimirDados() + f'\nRendimento da Pupança: {self.rendimento}'

    def cadastrar(self, nome, cpf, saldo, rendimento):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.rendimento = rendimento

    def depositar(self):
        return self.depositar()