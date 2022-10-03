from ctypes.wintypes import PINT
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente

c1 = ContaPoupanca()
c1.cadastrar('Saul', 10356209023, 100, 10)
print(c1.imprimirDados())

print('--------------------------------')

c2= ContaCorrente()
c2.cadastrar("Jose", 29812345673, 3000, 2)
print(c2.imprimirDados())