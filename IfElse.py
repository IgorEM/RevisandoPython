a= int(input('Entre com o Primeiro valor: '))
b= int(input('Entre com o Segundo valor: '))
c= int(input('Entre com o Terceiro valor: '))
d= int(input('Será que é par?: '))

if a > b and a > c :
    print('\no maior número é: {}'.format(a))
elif b > a and b > c:
    print('\no maior número é: {}'.format(b))
else:
    print('\no maior número é {}'.format(c))


if d%2 == 0:
    print("O número {} é par".format(d))
else:
    print("O número {} não é par".format(d))

print("\nFinal do Programa :D ")


