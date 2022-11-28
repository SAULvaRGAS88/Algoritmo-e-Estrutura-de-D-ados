class Torre:

    def __init__(self, id=None, nome=None, endereco=None):
        self.id = id
        self.none = nome
        self.endereco = endereco
        print('Torre Contruida')

    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        return print(f'\n Id Cadastrado {self.id}, Torre {self.nome} cadastrada no endereço {self.endereco}')