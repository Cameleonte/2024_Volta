def somma_elementi(lista, somma=0):
    if len(lista) == 0:
        return somma
    else:
        somma += lista[0]
        lista.pop(0)
        return somma_elementi(lista, somma)


lista_elementi = [int(x) for x in input('Inserisci gli elementi per qui vuoi calcolare la somma, divisi'
                                        'uno dall\'altro solo da uno spazio: ').split()]

somma_totale = somma_elementi(lista_elementi)
print(somma_totale)
