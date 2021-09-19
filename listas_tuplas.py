lista = [1,3,5,7]
lista_animal = ["cachorro","gato","elefante"]

#print(type(lista))
#print(lista_animal[2])

# soma = 0
# for x in lista:
#     print(x)
#     soma = soma + x
#     print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(max(lista_animal))
# print(min(lista_animal))

# nova_lista = lista_animal * 3
# print(nova_lista)


def incluir_animal(x):
    if x in lista_animal:
        print("{} já está na lista de animais".format(x))
    else:
        print("{} não está na lista, mas será adicionado ao final dela".format(x))
        lista_animal.append(x)
        print(lista_animal)

# incluir_animal('gato')
# incluir_animal('cachorro')

# lista_animal.append('lobo')

lista_animal.pop()
lista_animal.pop()

lista_animal.append('elefante')
lista_animal.append('arara')
lista_animal.append('peixe')
passaros = ["piriquito","papagaio","canario"]

for i in passaros:
    lista_animal.append(i)

# lista_animal.sort()


lista_animal[0] = 'borboleta'
print(lista_animal)

#tupla não altera valor

tupla = (1,10,12,14)
print(tupla)
print(len(tupla))

tupla_animal = tuple(lista_animal)

print(tupla_animal)
print(type(tupla_animal))

conv_lista = list(tupla)
print(conv_lista)

