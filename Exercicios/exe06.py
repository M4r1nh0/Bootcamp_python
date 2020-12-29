i = 1
soma = 0
while i <= 5:
    numero = int(input('numero '))
    soma += numero
    if i == 5:
        calculo = soma/i
    i += 1

print("a média do numeros numeros é igual a {}".format(calculo))
