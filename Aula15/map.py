def getTamanho(x):
    return len(x)

# def aumentaPreco(p):
#     return p * 1.1

# frutas = ["Laranja", "Banana", "Melancia"]
carros = ("Corsa", "Palio", "Corolla", "Savero", "Fusca", "Meriva")

# tamanhoFrutas = map(getTamanho, frutas)
# print("Frutas:",list(tamanhoFrutas))

tamanhoCarro = map(getTamanho, carros)
print("CARRO:",list(tamanhoCarro))

# precos = [6.0, 5.50, 4.99, 10.80]

# novosPrecos = map(aumentaPreco, precos)
# print("Novos Preços:", list(novosPrecos))

# produto = {
#     0: 10.0,
#     1: 5.0,
#     5: 1.5
# }

# print(produto)

# novoProduto = map(aumentaPreco, produto)
# print(list(novoProduto))

# novoProduto = map(aumentaPreco, produto.values())
# print(list(novoProduto))

