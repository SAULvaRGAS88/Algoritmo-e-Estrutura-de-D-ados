from Automovel import Automovel


class Moto(Automovel):
    def __init__(self, marca=..., qtdRodas=..., modelo=..., velocidade=0, potenciaMotor=..., partidaEletrica=bool):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaMotor)
        self.partidaEletrica = partidaEletrica
        print('Moto criada')

    def imprimirInfo(self):
        super().imprimirInfo()
        print('Este veiculo possui partida Eletrica? ', self.partidaEletrica)

    def acelar(self):
        return super().acelar(self.velocidade)

    def frear(self):
        return super().frear(self.velocidade)