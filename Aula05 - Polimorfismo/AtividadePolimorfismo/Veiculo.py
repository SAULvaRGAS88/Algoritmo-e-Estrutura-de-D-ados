class Veiculo:

    def __init__(self, marca=str, qtdRodas=int, modelo=str, velocidade=0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
        print('Veiculo construido')

    def imprimirInfo(self):
        print("Marca do veiculo: ", self.marca)
        print("Quantidade de rodas: ", self.qtdRodas)
        print("Modelo do veiculo: " ,self.modelo)
        print("Velocidade: ", self.velocidade,'km')

    def acelar(self):
        return self.acelar(+self.velocidade)
        

    def frear(self):
        return self.frear(-self.velocidade)
