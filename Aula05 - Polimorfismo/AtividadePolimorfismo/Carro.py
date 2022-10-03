from Automovel import Automovel

class Carro (Automovel):
    def __init__(self, marca=..., qtdRodas=..., modelo=..., velocidade=0, potenciaMotor=..., qtdPortas=int):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaMotor)
        self.qtdPortas=qtdPortas
        print('Carro criado')

    def imprimirInfo(self):
        super().imprimirInfo()
        print('Carro Possoi ', self.qtdPortas)

    def acelar(self):
        return super().acelar()

    def frear(self):
        return super().frear()