from Veiculo import Veiculo


class Automovel (Veiculo):
    def __init__(self, marca=..., qtdRodas=..., modelo=..., velocidade=0, potenciaMotor=float):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potenciaMotor = potenciaMotor
        print('Automovel Criado')

    def imprimirInfo(self):
        super().imprimirInfo()
        print("Veiculo possou um motor de ", self.potenciaMotor, "cc")

    def acelar(self):
        return super().acelar()

    def frear(self):
        return super().frear()