class Pessoa():

    __slots__ = ['_nome' , '_cpf' , '_nascimento' , '_endereco' , '_telefone' , '_email']
    
    def __init__(self):
        self._nome = None
        self._cpf = None
        self._nascimento = None
        self._endereco = None
        self._telefone = None
        self._email = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self , novo_nome):
        self._nome = novo_nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self , novo_cpf):
        self._cpf = novo_cpf

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self , nova_data):
        self._nascimento = nova_data

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self , novo_endereco):
        self._endereco = novo_endereco

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self , novo_telefone):
        self._telefone = novo_telefone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self , novo_email):
        self._email = novo_email    
