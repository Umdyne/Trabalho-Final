class Venda():

    __slots__ = ['_id' , '_data' , '_id_Usuario' , '_id_Produto' , '_quantidade']

    def __init__(self):
        self._id = None
        self._data = None
        self._id_Usuario = None
        self._id_Produto = None
        self._quantidade = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def id_Usuario(self):
        return self._id_Usuario

    @id_Usuario.setter
    def id_Usuario(self, usuario):
        self._id_Usuario = usuario

    @property
    def id_Produto(self):
        return self._id_Produto

    @id_Produto.setter
    def id_Produto(self, produto):
        self._id_Produto = produto

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade    
