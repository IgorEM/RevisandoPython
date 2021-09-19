lista = [0,1]
arquivo = open('teste.txt','r')

try:
    divisao = 10 / 1 #se der erro aqui ele nao executa nada que tá abaixo
    numero = lista[1]
    x = 1
    # print('Fechando Arquivo')
    # arquivo.close()
# except Exception as ex: #exception tree python
#     print('erro desconhecido. Erro: {}'.format(ex))
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
# except NameError:
#     print('nome a não está definido')
except BaseException as ex: #arvore de exceções
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Excecuta quando não ocorre exceção')
finally:
    print('Sempre Executa')
    print('Fechando Arquivo')
    arquivo.close()