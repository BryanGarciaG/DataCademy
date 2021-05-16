import math


def volumen_cilindro():
    print("Bienvenido al programa para calcular el volumen de un cilindro")
    radio = float(input("Por favor ingrese el radio de la base del cilindro: "))
    altura = float(input("Por favor ingrese la altura del clindro: "))

    area_base = math.pi * radio**2
    volumen = round(area_base * altura, 2)

    print(f"El volumen de tu cilindro es {volumen}")


def volumen_cubo():
    print("Bienvenido al programa que cualcula el volumen de un cuadrado")
    lado = float(input("Por favor ingrese la medida de uno de los lados"))
    volumen = round(lado**3, 2)
    print(f"El volumen del cubo es {volumen}")


def volumen_piramide():
    print("Bienvenido al programa que cualcula el volumen de una piramide")
    base = float(input("Ingrese la base: "))
    altura_base = float(input("Ingrese la altura de la base: "))
    altura_piramide = float(input("Ingrese la altura de la piramide"))

    area_base = (base * altura_base) / 2
    volumen_piramide = round(area_base * (1/3 * altura_piramide), 2)
    print(f"El volumen de la piramide es {volumen_piramide}")


def run():
    menu = f"""Bienvenido al programa para calcular el volumen de diferentes cuerpo:
        1) Cilindro
        2) Cubo
        3) Piramede
    Selecciona un cuerpo por favor: """
    opcion = int(input(menu))

    if opcion == 1:
        volumen_cilindro()
    elif opcion == 2:
        volumen_cubo()
    elif opcion == 3:
        volumen_piramide()
    else:
        print("Seleccione una opcion valida")


if __name__ == "__main__":
    run()
