#pais_A = 400000
#pais_B = 100000
#resultado 95
pais_A = int(input("numero maior "))
pais_B = int(input("numero menor "))
crescimento_A = float(input("cres A "))
crescimento_B = float(input("cres B "))
contagem = 0
while pais_B < pais_A:
    calculo = (crescimento_B*pais_B)/100
    calculoA = (crescimento_A*pais_A)/100
    pais_A += calculoA
    pais_B += calculo
    contagem += 1
    if pais_B >= pais_A:
        print("Em {} anos o pais_B vai alcançar o pais_A".format(contagem))
        print("O calculo {}".format(calculo))
        print("Os anos {}".format(contagem))
