from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro
from Moto import Moto

v1 = Veiculo("BMW", 4, "AUto", 100)
v1.imprimirInfo()
print('-----------')
b1 = Bicicleta("xxx", 2, "bice", 25, 21, False)
b1.imprimirInfo()
print('-----------')
a1 = Automovel("Fiat", 4, "Uno", 60, 1.0)
a1.imprimirInfo()
print('-----------')
c1 = Carro("GM", 4, "Omega", 40, 2.2, 4)
c1.imprimirInfo()
print('-----------')
m1 = Moto("Honda", 2, "twyster", 130, 250, True)
print(m1.acelar())
print(m1.frear())
m1.imprimirInfo()
