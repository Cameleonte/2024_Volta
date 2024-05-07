def torre_di_hanoi(a, piolo1, piolo2, piolo3):
    if a == 1:
        print(f'Sposta disco 1 da {piolo1} a {piolo3}')
        return
    torre_di_hanoi(a - 1, piolo1, piolo3, piolo2)
    print(f'Sposta disco {a} da {piolo1} a {piolo3}')
    torre_di_hanoi(a - 1, piolo2, piolo1, piolo3)


n = int(input('Inserire un numero di dischi sul piolo di partenza: '))
torre_di_hanoi(n, 'A', 'B', 'C')
