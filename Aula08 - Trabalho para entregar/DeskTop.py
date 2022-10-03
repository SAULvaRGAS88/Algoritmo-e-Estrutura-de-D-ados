from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo= None, cor= None, valor= None, potenciaDaFonte= None):
        super().__init__(modelo, cor, valor)
        self._potenciaDaFonte = potenciaDaFonte
        print('DeskTop Construido')

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        self._ = valor
    
    def getInformacoes(self):
        return super().getInformacoes() + f'\nPotencia da fonte: {self._potenciaDaFonte}'

    def cadastrar(self, modelo, cor, valor, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self._potenciaDaFonte = potenciaDaFonte
