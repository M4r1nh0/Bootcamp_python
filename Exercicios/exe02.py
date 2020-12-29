user = input("Digite seu nome de usuario: ")
senha = input("Digite sua senha: ")

while user == senha:
    print('[*] Não use o nome de usuario como senha [*]')
    senha = input("Por favor troque sua senha: ")
    if senha != user:
        print('Senha valida, Obrigado!')
