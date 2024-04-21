def inserendo_lista():
    lista_principale = []
    lista_corrente = [int(x) for x in input(f'Inserisci una lista da numeri positivi interi, '
                                            f'divisi da uno solo spazio: ').split()]
    lista_corrente.sort()
    while lista_corrente:
        numero_massimo = max(lista_corrente)
        numero_minimo = min(lista_corrente)
        if len(lista_corrente) <= 1:
            lista_principale.append(lista_corrente[0])
            break
        lista_principale.append(numero_massimo)
        lista_principale.append(numero_minimo)
        lista_corrente.remove(numero_massimo)
        lista_corrente.remove(numero_minimo)
    return lista_principale


lista = ', '.join(map(str, inserendo_lista()))
print(f"La lista ordinata secondo i criteri è: {lista}")
