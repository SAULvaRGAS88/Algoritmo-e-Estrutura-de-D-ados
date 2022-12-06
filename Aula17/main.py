#construir uma pilha de livro para dar baixa nos emprestimos
# o livro deve conter relação com os autores cadastrados
from Autor import Autor
from Livro import Livro
from Pilha import Pilha

a1 = Autor("Érico Verissimo", 98)
a2 = Autor("Fernando pessoa", 120)
l1 = Livro("O tempo e o vento", 250, a1)
l2 = Livro("O continente", 120, a1, "Capa dura")
l3 = Livro("Tabacaria", 120, a2 )

livros = Pilha()
livros.imprimir()
livros.adicionarLivro(l2)
print("=====================")
livros.adicionarLivro(l1)
