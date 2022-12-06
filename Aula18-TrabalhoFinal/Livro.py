from Publicacao import Publicacao 
class Livro (Publicacao):
    def __init__(self, id, anoPublicacao, titulo, autor):
        super().__init__(id, anoPublicacao)
        self.titulo = titulo
        self.__autor = autor

    @property
    def autor(self):
        if self.__autor != None:
            return self.__autor
        else:
            return None

    @autor.setter
    def autor(self, autor):
        if autor != None:
            self.__autor = autor

    def cadastrar(self):
        print("O livro foi cadastrado")

    def __str__(self):
        texto = super().__str__() + f"\nTitulo:  { self.titulo}  \nAutor: {self.__autor}"
        return texto        

  