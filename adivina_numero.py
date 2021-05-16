import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = 0

    while numero_aleatorio != numero_usuario:
        numero_usuario = int(input("Ingresa un numero "))
        if numero_usuario > numero_aleatorio:
            print("Busca un numero mas pequeño")
        elif numero_usuario < numero_aleatorio:
            print("Busca un numero mas grande")
        else:
            print(f"Ganaste!!! el numero {numero_usuario} es el que estabas buscando")
            break


if __name__ == "__main__":
    run()
