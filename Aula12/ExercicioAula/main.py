#FILA DE CARRO DE UMA LAVAGEM

from Fila import Fila

fifo = Fila()
fifo.add('ABC-1234', 43209837)
fifo.add('BCV-1234', 97832832)
fifo.add('ASS-1234', 99876654)

fifo.remover()
fifo.remover()
fifo.add('XXX-1234', 99876654)
fifo.remover()
fifo.remover()
