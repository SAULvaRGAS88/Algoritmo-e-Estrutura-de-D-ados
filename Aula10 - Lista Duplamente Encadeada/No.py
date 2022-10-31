# Construa o algoritmo em Python de uma lista
# duplamente encadeada que possui uma função para
# inserir elementos em ordem alfabética, uma função para
# imprimir os elementos da lista e uma função para
# imprimir os elementos na ordem inversa.

class No:
    def __init__(self, dado, anterior, proximo):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo