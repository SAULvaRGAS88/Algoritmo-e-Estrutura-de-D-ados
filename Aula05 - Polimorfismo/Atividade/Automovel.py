from veiculo import Veiculo


from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, potenciaMotor):
        super().__init__(potenciaMotor)


    def potenciaMotor(self):
        return self.potenciaMotor

    def imprimirInfo(self):
        return super().imprimir()
