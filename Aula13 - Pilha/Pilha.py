from Livro import Livro


class Pilha:
    def __init__(self):
        self.topo = None

    def adicionar(self, titulo):
        livro = Livro(titulo)
        if not self.topo:
            self.topo = livro
        else:
            novo_nodo = self.topo
            self.topo = novo_nodo

    def remover(self):
        if self.topo == None:
            print('Lista Vazia')
        else:
            self.topo = self.topo.proximo

    def imprimir(self):
        if not self.topo == None:
            print("Lista vazia!\n-------")
        else:
            print('=============')
            aux = self.topo
            while aux:
                print(f'Livro: {aux.titulo}\n')
                aux = aux.proximo
