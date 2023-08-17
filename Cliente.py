from Pessoa import Pessoa

class Cliente(Pessoa):

    __slots__ = ['_login' , '_senha']

    def __init__(self):
        super().__init__()
        self._login = None
        self._senha = None

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





