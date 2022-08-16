produtos = ["coca-cola", "Pepsi", "Chetos"]
precos = [7.79, 5.99, 3.58]
quantidade = [100, 50, 75]


def imprimir(posicao):
    print("nome: " , produtos[posicao])
    print("Preço: " , precos[posicao])
    print("Quantidade: " , quantidade[posicao])

def imprimirTodos():
    for i in range (len(produtos)):
        print("nome: " , produtos[i])
        print("Preço: " , precos[i])
        print("Quantidade: " , quantidade[i])
        print("------------------")


def remover(posicao):
    produtos.pop(posicao)
    precos.pop(posicao)
    quantidade.pop(posicao)
    imprimirTodos()

print (" 1 - Imprinr um produto da lista")
print (" 2 - Excluir um produto da lista")

opcao = int (input("Digite sua Opção: "))
pocicao = int (input("Digite a posição: "))

if opcao == 1:
    imprimir(pocicao)
elif opcao == 2:
    remover(pocicao)
else:
    imprimirTodos()