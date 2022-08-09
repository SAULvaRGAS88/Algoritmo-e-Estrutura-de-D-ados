# NomeProduto  = ["cafe", "sal", "laranja"]

# def imprimir(NomeProduto):
#     print(NomeProduto)

# imprimir(NomeProduto[0])


# def removerItem(NomeProduto):
#     print(NomeProduto)
# NomeProduto.remove(NomeProduto[2])

# removerItem(NomeProduto)

# ###############################################


# NomeProduto = ["cafe", "sal", "laranja"]
# PrecoProduto = [5.50, 2, 4]
# QuantidadeProduto =[10, 50, 15]

# def imprimir(list):
#  print(NomeProduto[0])
#  print(PrecoProduto[0])
#  print(QuantidadeProduto[0])

# def remover(index):
#  NomeProduto.pop(index)
#  PrecoProduto.pop(index)
#  QuantidadeProduto.pop(index)

# index = input("digite a posição que quer imprimir e/ou deletar das listas: ")
# imprimir(index)
# remover(index)

#####################################################

# lista1 = ["cafe", "sal", "laranja"]
# lista2 = [5.50, 2, 4]
# lista3 = [10, 50, 15]


# def imprimir(index):
#     print(lista1[index])
#     print(lista2[index])
#     print(lista3[index])


# def remover(index):
#     lista1.pop(index)
#     lista2.pop(index)
#     lista3.pop(index)


# index = input("digite a posição que quer imprimir e/ou deletar das listas: ")
# imprimir(index)
# remover(index)

########################################################

NomeProduto = ["cafe", "sal", "laranja"]
PrecoProduto = ["5", "2", "4"]
QuantidadeProduto = ["10", "50", "15"]

def imprimir(NomeProduto):
   print(NomeProduto[1])
   print(PrecoProduto[1])
   print(QuantidadeProduto[1])


def remover():
    NomeProduto.pop()
    PrecoProduto.pop()
    QuantidadeProduto.pop()
    return NomeProduto

imprimir(NomeProduto)
remover()
imprimir(NomeProduto)


# def imprimirProduto(PrecoProduto):
#     return(PrecoProduto)

# def imprimirQuantidade(QuantidadeProduto):
#     return(QuantidadeProduto)

# print(
#     f'O produto {NomeProduto[1]} custa {PrecoProduto[1]} e tem {QuantidadeProduto[1]} unidades')

# def removerItem(NomeProduto):
#     return(NomeProduto)

# NomeProduto.remove("cafe")

# imprimirNome(NomeProduto)
# print(NomeProduto)
