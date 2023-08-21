from datetime import datetime
from Sistema import Sistema
from Pessoa import Pessoa
from Cliente import Cliente
from Produto import Produto
import re

sistema = Sistema()
usuario = Cliente()
usuario.nome = 'usuario1'
usuario.cpf = 1
usuario.login = '1'
usuario.senha = '1'
sistema.usuarios = usuario

produto1 = Produto()
produto2 = Produto()
produto1.id = 1
produto1.nome = "produto1"
produto1.quantidade = 10
produto1.preco = 10
produto1.fornecedor = "fornecedor1"

produto2.id = 2
produto2.nome = "produto2"
produto2.quantidade = 10
produto2.preco = 12.5
produto2.fornecedor = "fornecedor2"

sistema.produtos = produto1
sistema.produtos = produto2





