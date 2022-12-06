from Impresso import Impresso 
class Livro (Impresso):
    def __init__(self, titulo="Sem Titulo", qtdPaginas=1, autor= None, capa=None):
        super().__init__(titulo, qtdPaginas, autor)
        self.capa = capa

    def cadastrar(self):
        print("O livro foi cadastrado")

    def __str__(self):
        return super().__str__() + f"\nCapa:  { self.capa}"

    