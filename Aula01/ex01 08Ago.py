"""Construir um algoritmo que contenha 3 listas, cada lista contendo:
• Nomes de produtos
• Preços de cada produto
• Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas. As funções devem receber
um parâmetro que será usado para acessar a posição dos itens das listas
que serão impressos ou retirados."""
NomeProduto = ["cafe", "sal", "laranja"]
PrecoProduto = [5.50, 2, 4]
QuantidadeProduto = [10, 50, 15]


def imprimirNome(NomeProduto):
    return(NomeProduto)


def imprimirProduto(PrecoProduto):
    return(PrecoProduto)


def imprimirQuantidade(QuantidadeProduto):
    return(QuantidadeProduto)


print(
    f'O produto {NomeProduto[1]} custa {PrecoProduto[1]} e tem {QuantidadeProduto[1]} unidades')


def removerItem(NomeProduto):
    return(NomeProduto)


NomeProduto.remove("cafe")

imprimirNome(NomeProduto)
print(NomeProduto)
