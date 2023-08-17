from Cliente import Cliente
from Funcionario import Funcionario
from Administrador import Administrador
from Produto import Produto


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
        
    opcao = None
    
    while opcao != 0:
        print('main')
        opcao = menu(1)
    
sistema()    
