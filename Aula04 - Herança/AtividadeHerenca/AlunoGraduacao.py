from Aluno import Aluno


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre=int):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre
        print('Aluno Graduação ativo')

    def imprimir(self):
        print('Codigo Aluno: ', self.codigo)
        print('Nome do Aluno: ', self.nome)
        print('Matricula Aluno: ', self.matricula)
        print('Aluno no semestre: ', self.semestre)
