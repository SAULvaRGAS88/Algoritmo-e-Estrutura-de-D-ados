def getPi():
    return 3.14


def imprimePi():
    print(getPi())


def calculaAreaCirculo(raio):
    return getPi() * (raio * raio)

def imprimiAreaCirculo(raio):
    print(calculaAreaCirculo(raio))


imprimiAreaCirculo(3)    