from No import No


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None


def inserirPrimeiraLetra(self, novaLetra):
    no = No(novaLetra)
    if self.inicio or self.fim:
        temp = self.inicio
        aux = temp
        while temp:
            if ord(no.dado) >= ord(temp.dado):
                aux = temp
            else:  # ord(no.dado) < ord()
                if temp.proximo == None:
                    temp.proximo = no
                temp.anterior = no
                no.proximo = temp
                aux.proximo = no
                no.anterior = temp
                self.fim = no

            temp = temp.proximo


def imprimir(self):
    pass


def remover(self, valor):
    if self.inicio == None:
        print('lista vazia ')
    else:
        if self.inicio.proximo == None and self.inicio.dado == valor:
            self.inicio = None
            self.fim = None
        else:
            if self.inicio.dado == valor:
                self.inicio.proximo.anterior = None
                self.inicio = self.inicio.proximo

            else:
                aux = self.inicio
                temp = self.inicio.proximo
                while (temp):
                    if temp.dado == valor:
                        if temp.proximo == None:
                            self.fim = aux
                        else:
                            temp.proximo.anterior = aux
                        aux.proximo = temp.proximo
                        break
                    temp = temp.prximo