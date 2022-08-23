from Cidade import Cidade
from Endereco import Endereco
from Pessoa import Pessoa

end = Endereco ("Bairro")
city = Cidade("POA")
p1 = Pessoa("Saul" , city, end)

p1.imprimir()