lato1 = int(input('Inserisci la lunghezza del primo lato: '))
lato2 = int(input('Inserisci la lunghezza del secondo lato: '))
lato3 = int(input('Inserisci la lunghezza del terzo lato: '))

if lato1 != lato2 and lato1 != lato3 and lato2 != lato3:
    print('Il triangolo con questi lati è scaleno.')
elif (lato1 == lato2 and lato1 != lato3) or (lato1 == lato3 and lato1 != lato2) or (lato3 == lato2 and lato3 != lato1):
    print('Il triangolo con questi lati è isoscele.')
else:
    print('Il triangolo con questi lati è equilatero.')
