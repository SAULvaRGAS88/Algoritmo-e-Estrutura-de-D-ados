""" Construa um algoritmo de busca contendo um vetor de números
inteiros de 20 posições.
• O algoritmo deve ter duas funções, uma para busca sequencial e
outra para busca binária.
• Coloque um contador em cada função para contar as iterações de
cada função.
• Peça ao usuário que informe o valor que deseja procurar.
• Então informe ao usuário se este valor existe no vetor e quantas
iterações foram necessárias em cada função."""


def buscaSequencial(lista, chave):
    cont = 0
    for i in range(len(lista)):
        cont = cont + 1
        if lista[i] == chave:
            print("O numero", chave, 'esta na posição', i)
            print('Numeros de iteraçoes:', cont)
            break
    else:
        print("Número", chave, "não encontrado na lista")


def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    cont = 0
    while inicio <= fim:
        meio = (inicio + fim)//2
        cont = cont + 1
        if lista[meio] == chave:
            print('Número digitado:', chave, cont ,'iteraçoes')
            break
        elif lista[meio] > chave:
            fim = meio - 1
        else:
            inicio =  meio + 1
    else:
        print("Número", lista, "não encontrado na lista")


chave = int(input("Digite um número: "))
lista = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]
print(">>>BUSCA SEQUENCIAL<<<")
buscaSequencial(lista, chave)
print(">>>BUSCA BINARIA<<<")
buscaBinaria(lista, chave)
