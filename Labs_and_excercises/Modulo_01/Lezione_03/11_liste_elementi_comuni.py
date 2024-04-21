def confrontare_liste(lista1):
    lista_elementi_comuni = []
    for elem in lista1[0]:
        if elem in lista1[1] and elem in lista1[2]:
            lista_elementi_comuni.append(elem)
    return lista_elementi_comuni            


def inserire_liste():

    # Quì le liste vanno inserite, messi in ordine ascendente e messi insieme in una lista principale

    lista_principale = []
    for num in range(1, 3 + 1):
        lista_corrente = [float(x) for x in input(f'Inserisci lista{num} da numeri divisi solo da uno spazio: ').split()]
        lista_corrente.sort()
        lista_principale.append(lista_corrente)
    return lista_principale


lista = inserire_liste()
elementi_comuni = confrontare_liste(lista)

print(f'Le tre liste inserite sono: ')
for lista_a in lista:
    lista_per_stampa = ' '.join(map(str, lista_a))
    print(f'{lista_per_stampa}')

stampa1 = ', '.join(map(str, elementi_comuni))
print(f'Gli elementi comuni nelle tre liste sono: {stampa1}')
