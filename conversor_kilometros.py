def run():

    KM_MILLA = 1.60934
    menu = """Bienvenido al conversor de millas y kilometros
    ¿Que unidad deseas convertir?
    1) Millas a Kilometros
    2) Kilometros a Millas

    Seleccione una opcion: """
    menu_dicc = {
        1: "Millas a Kilometros",
        2: "Kilometros a Millas"
    }

    opcion = int(input(menu))
    if opcion == 1:
        valor_convercion = float(input(f"Ingrese valor a convertir de {menu_dicc.get(1)} "))
        resultado = round((valor_convercion * KM_MILLA), 2)
        print(f"{valor_convercion} son {resultado} millas")
    else:
        valor_convercion = float(input(f"Ingrese valor a convertir de {menu_dicc.get(2)} "))
        resultado = round((valor_convercion / KM_MILLA), 2)
        print(f"{valor_convercion} son {resultado} millas")


if __name__ == "__main__":
    run()
