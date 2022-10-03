from Veiculo import Veiculo


class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas= int, bagageiro=bool):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
        print('Bicicleta construido')

    def imprimirInfo(self):
        super().imprimirInfo()
        print("A bice tem ", self.numMarchas , "marchas")
        print("A Bice possui Bagageiro? ", self.bagageiro)

    def acelar(self):
        return super().acelar()

    def frear(self):
        return super().frear()
            
