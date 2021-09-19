contador_letras = lambda lista: [len(x) for x in lista]


lista_frutas = ['acerola','abacaxi','goiaba']
print(contador_letras(lista_frutas))


soma = lambda a,b: a + b
subtracao = lambda a,b: a - b
print(soma(5,10))
print(subtracao(10,5))