def getTamanho(x):
    return len(x)

def aumentaPreco(p):
    return p * 1.1

frutas = ["Laranja", "Banana", "Melancia"]
jogadores = ("Maria", "José", "Júlia", "Carlos", "Joana", "Marcelo")

tamanhoFrutas = map(getTamanho, frutas)
print("Frutas:",list(tamanhoFrutas))

tamanhoJogadores = map(getTamanho, jogadores)
print("Frutas:",list(tamanhoJogadores))

precos = [6.0, 5.50, 4.99, 10.80]

novosPrecos = map(aumentaPreco, precos)
print("Novos Preços:", list(novosPrecos))

produto = {
    0: 10.0,
    1: 5.0,
    5: 1.5
}

print(produto)

novoProduto = map(aumentaPreco, produto)
print(list(novoProduto))

novoProduto = map(aumentaPreco, produto.values())
print(list(novoProduto))

