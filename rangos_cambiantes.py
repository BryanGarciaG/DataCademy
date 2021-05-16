def run():
    print("Bienvenido al Juego de Rangos")

    salir = ""

    while salir != "no":
        rango_inferior = int(input("Ingrese el rango inferior: "))
        rango_superior = int(input("Ingrese el rango superior: "))
        valor_comparacion = int(input("Ingrese valor Comparacion: "))

        if valor_comparacion >= rango_inferior and valor_comparacion <= rango_superior:
            print(f"{valor_comparacion} esta en el rango")
        else:
            print(f"{valor_comparacion} esta fuera de rango")
        salir = input("¿Desea continuar con el juego? ")  

    print("Hasta luego ;-)")


if __name__ == "__main__":
    run()
