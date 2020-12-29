base = int(input("base "))
expoente = int(input("expoente "))
i = 1
potencia = 1
while i <= expoente:
    #base * base
    potencia *= base
    i += 1
    print(potencia)
