carro = {
    "modelo": "Doblo",
    "ano": 2006,
    "reboque": False,
    "capacidade": 950.243
}

print(carro)

print("Ano: ", carro['ano'])

print(carro.keys())
print(carro.values())
print(carro.items())

for chave, valor in carro.items():
    print(chave, ":", valor)
print("-----------------------")
for chave in carro.keys():
    print(chave, ":", carro[chave])


print("--------Tupla de Dicionários---------------")

filho1 = {"nome": "Júlia", "idade": 14}
filho2 = {"nome": "Neymar", "idade": 30}
filho3 = {"nome": "Maurício", "idade": 22}

filhos = filho1, filho2
# filhos[0] = filho3
filho1["nome"] = "Maurício"
filho1["email"] = "m@m.com"
print(filhos[0])

del filho1['idade']

print(filhos)
