class Aluno:

    def __init__(self, codigo=int, nome=str, matricula=str):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        print('Aluno ativo')

    def imprimir(self):
        print('Codigo Aluno: ', self.codigo)
        print('Nome do Aluno: ', self.nome)
        print('Matricula Aluno: ', self.matricula)
