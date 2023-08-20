from Pessoa import Pessoa
from Cliente import Cliente
from Funcionario import Funcionario
from Administrador import Administrador
from Produto import Produto
from datetime import datetime
import re

def verifica_int(numero):

    try:
        numero = int(numero)
        return numero
    except:
        numero = input('Digite um numero valido: ')
        numero = verifica_int(numero)
        return numero
    
def verifica_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data.strftime('%d/%m/%Y')
    except ValueError:
        print("Data invalida.")
        return 1

def verifica_email(email):
    
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(padrao, email):
        return True
    else:
        return False



    
        
def menu(versao):

    if versao == 1:
        print("\n------MENU------")
        print("1 - Cadastrar um Cliente")
        print("2 - Cadastrar um Funcionario")
        print("3 - Cadastrar um Administrador")
        print("4 - Cadastrar um Produto")
        print("5 - Alterar/Remover um Produto")
        print("6 - Realizar uma venda")
        print("7 - Alterar Informações do usuario")
        print("8 - Alterar Informações de outro usuario")
    
    opcao = input("Selecione uma opcao: ")
    
    try:
        opcao = int(opcao)
        return opcao
    except:
        print('Selecione uma opção valida.')
        opcao = menu(2)
        
class Sistema():

    __slots__ = ['_usuarios' , '_vendas' , '_produtos']

    def __init__(self):
        self._usuarios = []
        self._vendas = []
        self._produtos = []

    @property
    def usuarios(self):
        return self._usuarios

    @usuarios.setter
    def usuarios(self, novo):
        self._usuarios.append(novo)


    def verifica_cpf(self , novo_cpf):
        if len(self.usuarios) != 0:
            for usuario in self.usuarios:
                print(usuario.cpf)
                if usuario.cpf == novo_cpf:
                    achou = 1
                else:
                    achou = 0

            if achou == 1:
                cpf = input("Esse cpf ja esta registrado, digite outro: ")
                cpf = verifica_int(cpf)
                cpf = self.verifica_cpf(cpf)
            
        return novo_cpf
    
    def cria_Pessoa(self):
        
        pessoa = Pessoa()
            
        pessoa.nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        cpf = verifica_int(cpf)
        cpf = self.verifica_cpf(cpf)
                    
        pessoa.cpf = cpf    
        nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
        pessoa.nascimento = verifica_data(nascimento)
        while pessoa.nascimento == 1:
            nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
            pessoa.nascimento = verifica_data(nascimento)
        pessoa.endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        pessoa.telefone = verifica_int(telefone)
        while len(str(pessoa.telefone)) != 11 :
            telefone = input("Digite um telefone valido: ")
            pessoa.telefone = verifica_int(telefone)
        pessoa.email = input("Digite o email: ")
        while verifica_email(pessoa.email) == False:
            pessoa.email = input("Digite um email valido: ")
        return pessoa.nome , pessoa.cpf , pessoa.nascimento , pessoa.endereco , pessoa.telefone , pessoa.email

    def add_Cliente(self):

        cliente = Cliente()
        pessoa = self.cria_Pessoa()

        cliente.nome = pessoa[0]
        cliente.cpf = pessoa[1]
        cliente.nascimento = pessoa[2]
        cliente.endereco = pessoa[3]
        cliente.telefone = pessoa[4]
        cliente.email = pessoa[5]
        cliente.login = input("Cadastre o login: ")
        cliente.senha = input("Cadastre a senha: ")

        cliente_D = { cliente.cpf : cliente }
        
        self.usuarios = cliente_D
        print("Cadastro realizado")
        
    def iniciar(self):
        opcao = None
        while opcao != 0:
            print('main')
            opcao = menu(1)

            if opcao == 1:
                self.add_Cliente()
  
sistema = Sistema()    
#sistema.iniciar()
