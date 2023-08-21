class Verificadores():
    
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

