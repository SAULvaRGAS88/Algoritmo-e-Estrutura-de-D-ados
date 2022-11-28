from Torre import Torre
from Apartamento import Apartamento
# from Fila import Fila

t = Torre ()
t.cadastrar(1, "01", "Assis Brasil")
t.imprimir()

a = Apartamento()
a.cadastrar(1, '101', Torre, 1, 'sim')
a.imprimir()