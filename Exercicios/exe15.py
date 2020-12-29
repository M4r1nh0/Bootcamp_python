i = 0
m = 0
while i < 4:
    n = int(input('nota '))
    i += 1
    m += n
    if i == 4:
        calculo = m/4
        print("a média é igual a {}".format(calculo))
