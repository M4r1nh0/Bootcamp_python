def contador_de_caracteres(s):
    caracteres_ordenadas = sorted(s.lower())
    caracter_anterior = caracteres_ordenadas[0]
    contagem = 1
    for caracter in caracteres_ordenadas[1:]:
        if caracter==caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior=caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    print(contador_de_caracteres("BaNaNa"))
