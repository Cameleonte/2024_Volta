import functools


def somma_pari(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n + somma_pari(n - 1)
    else:
        return somma_pari(n - 1)


def somma_dispari(n):
    if n == 1:
        return 1
    elif n % 2 != 0:
        return n + somma_dispari(n - 1)
    else:
        return somma_dispari(n - 1)    


@functools.lru_cache(maxsize=None)
def geometrica(n, a, b, acc=0):
    if n == 0:
        return acc + a
    else:
        acc += a * b ** n
        return geometrica(n-1, a, b, acc)
        

def func_principale():
    while True:
        print('\nScegli una delle opzioni: ')
        print('0 - Uscita')
        print('1 - La somma dei primi n numeri pari')
        print('2 - La somma dei primi n numeri dispari')
        print('3 - La seria geometrica con argomenti a, b, n')
        menu_principale = int(input('Inserisci la tua scelta: '))
        if menu_principale == 0:
            break
        elif menu_principale == 1:
            numero_x = int(input('Inserisci il numero per calcolare la somma dei pari: '))
            print(f'La somma dei numeri pari di {numero_x} è: {somma_pari(numero_x)}')
        elif menu_principale == 2:
            numero_x = int(input('Inserisci il numero per calcolare la somma dei dispari: '))
            print(f'La somma dei numeri dispari di {numero_x} è: {somma_dispari(numero_x)}')
        elif menu_principale == 3:
            numero_a = int(input('Inserisci il primo numero: '))
            numero_b = int(input('Inserisci il secondo numero: '))
            numero_n = int(input('Inserisci il numero del grado: '))
            serie = geometrica(numero_n, numero_a, numero_b)
            print(f'La serie geometrica di {numero_a}, {numero_b} e grado {numero_n} è: {serie}')
        else:
            print('Scelta non corretta. Riprova!')

    return


func_principale()
