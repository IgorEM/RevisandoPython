for num in range(7,15):
    div=0
    #todo número é divisivel por ele mesmo

    for x in range(1,num+1):
        resto = num % x
        #print("num: {}, x: {}, resto: {}".format(num,x,resto))
        if resto == 0:
            div = div + 1

    if div == 2:
        print('número {} é primo'.format(num))
