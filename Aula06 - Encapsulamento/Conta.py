class Conta:

    logado = True
    tarifa =1.99

    def __init__(self):
        self.__saldo = 0.0

    def __descontarTarifa(self):
        if self.__saldo >= self.tarifa:
            self.__saldo -= self.tarifa
            return True
        return False

    def depositar(self, valor):
        if self.__saldo + valor >= self.tarifa:
            self.__saldo += valor
            self.__descontarTarifa()
        else:
            print("Valor não permitio")

    def sacar(self, valor):
        if valor <= self.__saldo - self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()
        else:
            print("Saldo insuficiente")        

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if self.logado:
            self.__saldo = saldo


    # metodo acessor
    def getSaldo(self):
        self.logado = True
        if self.logado:
            return self. __saldo

    # metodo modificar
    def setSaldo(self, saldo):
        if self.logado:
            self.__saldo = saldo
