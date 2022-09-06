from Carro import Carro
from Veiculo import Veiculo
from Moto import Moto

v = Veiculo("GM" ,2017)
v.imprimir()

c = Carro("BMW", 2022, 4)
c.imprimir()
print("Portas:", c.qtdaPortas)

m = Moto("Honda", 2010, True)
m.imprimir()