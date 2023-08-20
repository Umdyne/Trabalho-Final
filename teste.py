from datetime import datetime
from Sistema import Sistema
from Pessoa import Pessoa
from Cliente import Cliente
import re




s = Sistema()

c = Cliente()
c.nome = 'Opa'
c.cpf = 1
s.usuarios = c
s.add_Cliente()



for n in s.usuarios:
    print(n.cpf)




