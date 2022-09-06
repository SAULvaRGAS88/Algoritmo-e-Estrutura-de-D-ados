
class Veiculo:

    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInfo(self):
        print("Marca do veiculo: ", self.marca)
        print("Quantidade de rodas: ", self.qtdRodas)
        print("Modelo do veiculo: " ,self.modelo)
        print("Velocidade: ", self.velocidade)

    def acelar(): pass

    def frear(): pass
