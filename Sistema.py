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

def verifica_float(numero):

    try:
        numero = float(numero)
        return numero
    except:
        numero = input('Digite um numero valido: ')
        numero = verifica_float(numero)
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
        print("0 - Sair")
    
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

    @property
    def vendas(self):
        return self._vendas

    @vendas.setter
    def vendas(self , nova_venda):
        self._vendas.append(nova_venda)

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, novo_produto):
        self._produtos.append(novo_produto)
        
    def verifica_cpf(self, novo_cpf):
        existe = False
        
        for usuario in self.usuarios:
            if usuario.cpf == novo_cpf:
                existe = True
                
        if existe:
            novo_cpf = input("Esse CPF já está registrado, digite outro: ")
            novo_cpf = verifica_int(novo_cpf) 
            novo_cpf = self.verifica_cpf(novo_cpf)
            retorno = novo_cpf
        else:
            retorno = novo_cpf

        return retorno
        
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

        self.usuarios = cliente
        print("Cadastro realizado")

    def add_Funcionario(self):

        funcionario = Funcionario()
        pessoa = self.cria_Pessoa()

        funcionario.nome = pessoa[0]
        funcionario.cpf = pessoa[1]
        funcionario.nascimento = pessoa[2]
        funcionario.endereco = pessoa[3]
        funcionario.telefone = pessoa[4]
        funcionario.email = pessoa[5]
        salario = input("Digite o salario: ")
        salario = verifica_int(salario)
        funcionario.salario = salario
        funcionario.login = input("Cadastre o login: ")
        funcionario.senha = input("Cadastre a senha: ")
        
        self.usuarios = funcionario
        print("Cadastro realizado")        

    def add_Administrador(self):

        administrador = Administrador()
        pessoa = self.cria_Pessoa()

        administrador.nome = pessoa[0]
        administrador.cpf = pessoa[1]
        administrador.nascimento = pessoa[2]
        administrador.endereco = pessoa[3]
        administrador.telefone = pessoa[4]
        administrador.email = pessoa[5]
        salario = input("Digite o salario: ")
        salario = verifica_int(salario)
        administrador.salario = salario
        administrador.login = input("Cadastre o login: ")
        administrador.senha = input("Cadastre a senha: ")
        
        self.usuarios = administrador
        print("Cadastro realizado")  

    def add_Produto(self):

        produto = Produto()
        
        produto.nome = input("Digite o nome do produto: ")
        produto.preco = input("Digite o preco do produto: ")
        produto.preco = verifica_float(produto.preco)
        produto.quantidade = input("Digite a quantidade do produto no estoque: ")
        produto.quantidade = verifica_int(produto.quantidade)
        produto.fornecedor = input("Digite o nome do fornecedor: ")
        produto.id = len(self.produtos) + 1
        self.produtos = produto
        print("Produto cadastrado")  

            

    def listar_Produtos(self):
        for produto in self.produtos:
                print("\nId: ",produto.id)
                print("Nome: ",produto.nome)
                print("Preço: ",produto.preco)
                print("Quantidade em estoque: ",produto.quantidade)
                print("Fornecedor: ",produto.fornecedor)

    def alterar_Produto(self):

        existe = False
        
        if len(self.produtos) == 0:
            print("Nenhum produto cadastrado. ")
            
        else:
            produto_Id = input("Digite o ID do produto ou digite 0 para listar: ")
            produto_Id = verifica_int(produto_Id)

            if produto_Id == 0:
                self.listar_Produtos()
                produto_Id = input("Digite o ID do produto: ")
                produto_Id = verifica_int(produto_Id)

            for produto in self.produtos:
                if produto_Id == produto.id:
                    produto.nome = input("Digite o novo nome do produto: ")
                    produto.preco = input("Digite o novo preco do produto: ")
                    produto.preco = verifica_float(produto.preco)
                    produto.quantidade = input("Digite a nova quantidade do produto no estoque: ")
                    produto.quantidade = verifica_int(produto.quantidade)
                    produto.fornecedor = input("Digite o novo nome do fornecedor: ")
                    print("Produto atualizado")
                    existe = True

            if existe == False:
                print("Produto não encontrado. ")
                

    def iniciar(self):
        opcao = None
        while opcao != 0:
            print('main')
            opcao = menu(1)

            if opcao == 1:
                self.add_Cliente()
                
            elif opcao == 2:
                self.add_Funcionario()
                
            elif opcao == 3:
                self.add_Administrador()

            elif opcao == 4:
                self.add_Produto()

            elif opcao == 5:
                self.alterar_Produto()    

            elif opcao == 6:
                self.realizar_Venda()
                
            elif opcao == 7:
                self.alterar_Info()

            elif opcao == 0:
                print("Saindo. ")

            else:
                print("Opção invalida. ")
  
sistema = Sistema()    
#sistema.iniciar()
