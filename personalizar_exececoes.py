class Error(Exception): #class Error herda de exceção que é uma classe que ja existe
    pass

class InputError(Error): # InputError herda de Error
    def __init__(self, message): #construtor
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            # raise força uma exceção
            raise InputError('nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('nota não pode ser menor que 0')
        break #sai do laço
    except ValueError:
        print('Valor inválido. Deve-se digiar apenas números. ')
    except InputError as ex:
        print(ex)
