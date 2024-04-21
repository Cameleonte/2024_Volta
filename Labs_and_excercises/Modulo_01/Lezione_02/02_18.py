spazio = ' '

for linea in range(1, 7):
    for sinistra in range(1, linea + 5):
        if sinistra > linea:
            print(spazio, end='')
        else:
            print(sinistra, end='')
    for destra in range(11 - sinistra, 0, - 1):
        print(destra, end='')
    print()
