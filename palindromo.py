def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabara para saber si es palindromo: ")
    isPalindromo = palindromo(palabra)
    if isPalindromo == True:
        print("La palabra " + palabra + " es un palindromo")
    else:
        print("La palabra " + palabra + " no es un palindromo")


if __name__ == '__main__':
    run()