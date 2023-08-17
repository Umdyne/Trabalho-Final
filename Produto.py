class Produto():

    __slots__ = ['_nome', '_id', '_preco', '_quantidade', '_fornecedor']

    def __init__(self):
        self._nome = None
        self._id = None
        self._preco = None
        self._quantidade = None
        self._fornecedor = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def fornecedor(self):
        return self._fornecedor

    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self._fornecedor = fornecedor    
