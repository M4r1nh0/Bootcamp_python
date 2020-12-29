nome = input("digite seu nome: ")
idade = int(input("digite a sua idade: "))
salario = int(input("digite o seu salario: "))


min = 'dan'

while True:
    if len(nome) <= len(min):
        print()
        print('digite um nome com mais caracteres! ')
        nome = input("digite um nome ")
    elif idade > 150 or idade == 0:
        print()
        print('idade invalida')
        idade = int(input('digite uma idade valida: '))

    elif salario == 0:
        print()
        print('salario invalido')
        salario = int(input('digite um salario valido: '))

    else:
        print()
        print("""todas as informações estão corretas!
        Seu nome é {}
        Sua idade é {}
        Seu salario é {}
        """.format(nome, idade, salario))
        break;
