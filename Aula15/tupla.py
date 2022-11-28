jogadores = "Maria", "José", "Júlia", "Carlos", "Joana", "Marcelo"

print(jogadores)

print(jogadores[2:-2])

# Não se pode mudar itens dentro de uma tupla:
# jogadores[1] = "Adalto"

print(jogadores)

for pessoa in jogadores:
    print(pessoa)

print(sorted(jogadores))

players = sorted(jogadores)
players[1] = "Adalto"
print(players)

def calcular(x,y):
    return (x+y), (x-y), (x*y), (x/y)

resultado = calcular(5,10)
print(resultado)
