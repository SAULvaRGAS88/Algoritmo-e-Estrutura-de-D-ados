from multiprocessing.spawn import import_main_path
from Endereco import Endereco
from Cidade import Cidade


class Pessoa:

    def __init__(self, nome, fone, endereco):
        self.nome = nome
        self.fone = fone
        self.endereco = endereco
    
    def imprimir (self):
        print ("Nome ", self.nome)
        print("Fone: ", self.fone)
        print("Endereço " , self.endereco)
    
    def cadastrar (nome, Cidade):
        return Cidade.getCidade()