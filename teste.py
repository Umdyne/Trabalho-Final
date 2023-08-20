from datetime import datetime
from Sistema import Sistema
from Pessoa import Pessoa
from Cliente import Cliente
from Produto import Produto
import re

s = Sistema()

c = Cliente()
c2 = Cliente()
c3 = Cliente()
c4 = Cliente()
c.nome = 'Pe1'
c.cpf = 1
c2.nome = 'Pe2'
c2.cpf = 2
c3.nome = 'Pe3'
c3.cpf = 3
c4.nome = 'Pe4'
c4.cpf = 4
s.usuarios = c
s.usuarios = c2
s.usuarios = c3
s.usuarios = c4

p = Produto()
p.nome = "produto1"
p.id = 1
p.quantidade = 10
p2 = Produto()
p2.nome = "produto2"
p2.id = 2
p2.quantidade = 20

s.produtos = p
s.produtos = p2


s.listar_Produtos()



