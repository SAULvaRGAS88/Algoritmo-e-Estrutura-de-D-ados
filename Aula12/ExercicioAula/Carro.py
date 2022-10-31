# app para lavagem de carro
# - placa - km
class Carro:

    def __init__(self, placa, km=0):
        self.placa = placa
        self.proximo = None
        self.km = km
