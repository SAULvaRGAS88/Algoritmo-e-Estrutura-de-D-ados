from Publicacao import Publicacao 
class Revista (Publicacao):
    def __init__(self, id, anoPublicacao, nome, preco):
        super().__init__(id, anoPublicacao)
        self.nome = nome
        self._preco = preco

    def cadastrar(self):
        print("A revista foi cadastrado")

    def __str__(self):
        texto = super().__str__() + f"\nPreço: { self._preco}"
        return texto