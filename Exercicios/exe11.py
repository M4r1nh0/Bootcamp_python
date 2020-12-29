n = int(input(": "))
i = 1
penultimo = 1
ultimo = 1
while i < n:
    calculo = penultimo + ultimo
    penultimo = ultimo
    ultimo = calculo
    i += 1
    print(calculo)
    if calculo > 500:
        print("passou de 500")
        break;
