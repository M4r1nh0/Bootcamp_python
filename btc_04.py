def contador_de_caracteres(s):
    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1



    return resultado

if __name__ == '__main__':
    print(contador_de_caracteres("banana"))
