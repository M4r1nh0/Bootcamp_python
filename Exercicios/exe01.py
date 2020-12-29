n1 = int(input('Digite um numero de 0 a 10: '))

while n1 > 10:
    print('[*] Numero invalido por favor, coloque um numero entre 0 e 10 [*]')
    n1 = int(input('Por favor digite um numero entre 0 e 10: '))
    if n1 <= 10:
        print('valor valido, Obrigado!')
