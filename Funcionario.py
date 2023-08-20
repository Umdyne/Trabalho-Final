from Pessoa import Pessoa

class Funcionario(Pessoa):

    __slots__ = ['_login' , '_senha' , '_salario']

    def __init__(self):
        super().__init__()
        self._login = None
        self._senha = None
        self._salario = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, novo_login):
        self._login = novo_login
        
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha
        
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        self._salario = novo_salario
