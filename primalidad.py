def es_primo(numero):
    valor_primo = True
    mitad_numero = round((numero/2))
    for i in range(1, mitad_numero):
        if i == 1:
            continue
        for j in range(1, numero):
            if j == 1:
                continue
            producto = i * j
            print(producto)
            if producto > numero:
                break
            elif producto == numero:
                valor_primo = False
                break
    return valor_primo


def run():
    numero = int(input("Escribe un numero "))
    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")


if __name__ == "__main__":
    run()
