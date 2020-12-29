n1 = int(input("nuemro "))
n2 = int(input("numero "))
soma = 0
contagem = 0
while n1 > n2:
    n1 = int(input("digite denovo "))
    n2 = int(input("digite denovo "))

else:
    for i in range(n1, n2):
        print()
        contagem += 1
        soma += i
        print(i)

calculo = soma/contagem
print(calculo)
