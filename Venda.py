class Venda():

    __slots__ = ['_id' , '_data' , '_id_Usuario' , '_info_Produtos']

    def __init__(self):
        self._id = None
        self._data = None
        self._id_Usuario = None
        self._info_Produtos = None

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
    def info_Produtos(self):
        return self._info_Produtos

    @info_Produtos.setter
    def info_Produtos(self, produto):
        self._info_Produtos = produto   
