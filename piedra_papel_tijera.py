import random


def run():
    opciones = ('piedra', 'papel', 'tijeras')
    puntos_maquina = 0
    puntos_jugador = 0

    for i in range(0, 3):
        jugador = input('Selecciona piedra, papel o tijeras ').lower().strip()
        maquina = opciones[random.randint(0, 2)]

        if(jugador == maquina):
            print(f"Empate. Maquina eligio {maquina}")
        elif((jugador == 'piedra' and maquina == 'papel') or (jugador == 'papel' and maquina == 'tijeras') or (jugador == 'tijeras' and maquina == 'piedra')):
            print(f"Maquina gana esta ronda, eligio {maquina}")
            puntos_maquina += 1
        else:
            print(f"Tu ganas esta ronda. Maquina eligio {maquina}")
            puntos_jugador += 1

        if puntos_maquina == 2 or puntos_jugador == 2:
            break

    if(puntos_jugador == puntos_maquina):
        print("Nadie gana el juego, es un empate")
    elif(puntos_maquina > puntos_jugador):
        print("Maquina gana el juego")
    else:
        print("Tu ganas el juego")     


if __name__ == "__main__":
    run()
