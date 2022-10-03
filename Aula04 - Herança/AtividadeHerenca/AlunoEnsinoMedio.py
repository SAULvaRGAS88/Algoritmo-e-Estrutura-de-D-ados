from Aluno import Aluno


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano=int):
        super().__init__(codigo, nome, matricula)
        self.ano = ano
        print('Aluno ensino médio Ativo')

    def imprimir(self):
        print('Codigo Aluno: ', self.codigo)
        print('Nome do Aluno: ', self.nome)
        print('Matricula Aluno: ', self.matricula)
        print('Aluno no ano: ', self.ano)
