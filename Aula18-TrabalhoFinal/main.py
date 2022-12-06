from Livro import Livro
from Pilha import Pilha
from Revista import Revista

l1 = Livro(123, 2020, "O vento e o tempo", "Érico verissimo")
l2 = Livro(444, 1876, "A mesa", "Desconhecido")

r1 = Revista(321, 1987, "Isto é", 10.99)
r2 = Revista(777, 1954, "Época", 19.99)

livros = Pilha()
livros.imprimir()
livros.adicionar(l1)
print('>>>>>>>>>>>>>>>><<<<<<<<<<<<')
livros.adicionar(l2)
livros.remover()
livros.imprimir()

print("=====================")


revista = Pilha()
revista.imprimir()
revista.adicionar(r1)
print('>>>>>>>>>>>>>>>><<<<<<<<<<<<')
revista.adicionar(r2)
livros.remover()
livros.imprimir()
print("FIM>>>>>>>>>>>")
