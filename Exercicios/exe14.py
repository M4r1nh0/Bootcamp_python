n = int(input('DIgite um numero '))
cont = 0
for c in range(1, n+1 ):
    if n%c == 0:
        print("O numero é divisivel por {}".format(c))
        cont +=1

if cont > 2:
    print("o numero {} não é primo".format(n))
else:
    print("o numero {} é primo ".format(n))
