def contador_letras(lista_palavras): #def
    lista1 = []
    for x in lista_palavras:
        contador = len(x)
        lista1.append(contador)
    return lista1

def teste():
    return 'teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato','elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista: {}'.format(total_letras))
