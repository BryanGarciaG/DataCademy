def run():
    print("Bienvenido al programa para calcular el área de un triangulo")
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    area = round(((base * altura)/ 2), 2)
    print(f"El area de tu triangulo es: {area}")
    equilatero = round(((3**0.5 / 4) * base**2), 2)
    print(f"El area de tu triangulo equilatero es: {equilatero}")


if __name__ == "__main__":
    run()