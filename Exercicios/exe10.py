i = 0
calculo = 0
quant_impares = 0
quant_pares = 0
while i < 10:
    n = int(input("digite um numero inteiro "))
    impar = n%2
    calculo += n
    if impar == 1:
        quant_impares += 1
    else:
        quant_pares += 1
    i += 1

print("O calculo de todos os numeros é {}".format(calculo))
print("Existem {} numeros impar".format(quant_impares))
print("Existem {} numeros pares".format(quant_pares))
