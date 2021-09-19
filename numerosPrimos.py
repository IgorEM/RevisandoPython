# for x in range(50, 101)

a = int(input('O número é primo?: '))
div=0
#todo número é divisivel por ele mesmo

for x in range(1,a+1):
    resto = a % x
    print("a: {}, x: {}, resto: {}".format(a,x,resto))
    if resto == 0:
        div = div + 1

if div == 2:
    print('número {} é primo'.format(a))
else:
    print('número {} não é primo'.format(a))
