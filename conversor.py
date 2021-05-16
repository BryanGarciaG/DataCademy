def conversor(tipo_moneda, tasa_conversion_dolares):
    pesos = input("¿Cuantos pesos " + tipo_moneda + " deseas convertir a dolares? ")
    pesos = round(float(pesos), 2)
    tasa_conversion_dolares = tasa_conversion_dolares
    dolares = round((pesos / tasa_conversion_dolares), 2)
    print("$" + str(pesos) + " pesos " + tipo_moneda + " son $" + str(dolares) + " dolares americanos")    


menu = """Bienvenido al programa de convesion de moneda
1 - Pesos Colombianos a Dolares.
2 - Pesos Argentinos a Dolares.
3 - Pesos Mexicanos a Dolares.

Por favor, selecciona una opcion para convertir: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Colombianos", 93)
elif opcion == 3:
    conversor("Colombianos", 19)
else:
    print("Selecciona una opción valida por favor")
