from Veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marcaCar, anoCar, portas):
        super().__init__(marcaCar, anoCar)
        self.qtdaPortas = portas
        print("Carro construido")