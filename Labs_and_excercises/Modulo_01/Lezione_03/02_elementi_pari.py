numeri = [float(x) for x in input('Inserisci una lista di numeri: ').split()]

nuova_lista = []
for num in numeri:
    if num % 2 == 0:
        nuova_lista.append(num)
print(f'I numeri pari sono: {nuova_lista}')
