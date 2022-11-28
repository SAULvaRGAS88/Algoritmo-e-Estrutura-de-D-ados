from Torre import Torre

class Apartamento:

    def __init__(self, id=None, numero=None, Torre=Torre, vaga=None, prox=None):
        self.id = id
        self.numero = numero
        self.torre = Torre
        self.vaga = vaga
        self.prox = Apartamento
        print('Apartamento Construido')

    def cadastrar(self, id, numero, Torre, vaga, prox):
        self.id = id
        self.numero = numero
        self.torre = Torre
        self.vaga = vaga
        self.prox= Apartamento

    def imprimir(self):
        return print(f'\n id cadastrado {self.id}, apartamento número {self.numero}, localizado na torre {Torre}, com {self.vaga} vaga(s)')
