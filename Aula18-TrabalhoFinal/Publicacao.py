from abc import ABCMeta, abstractmethod
class Publicacao (metaclass = ABCMeta):

    def __init__(self, id, anoPublicacao):
        self.id = id
        self.anoPublicacao = anoPublicacao
        self.proximo = None


    @abstractmethod
    def cadastrar(self):
        pass

    def __str__(self):
        texto = f"ID:   {self.id}  \nAno da Publicação: {self.anoPublicacao}"
        return texto