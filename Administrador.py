from Funcionario import Funcionario

class Administrador(Funcionario):

    __slots__ = []

    def __init__(self):
        super().__init__()

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario

