def run():
    contador = 0
    while contador < 1000000:
        contador += 1
        if contador % 2 == 0:
            continue
        if contador > 59631:
            break
        print(f'El numero {contador} es impar')


if __name__ == "__main__":
    run()
