def spostare_zero(lst):
    lista_zero = []
    for elem in lst:
        if elem == 0:
            lst.remove(elem)
            lista_zero.append(elem)
    lst += lista_zero

    return lst


def inserendo_lista():
    print(f'Inserire una lista da numeri divisi solo da uno spazio.')
    lista_corrente = [float(x) for x in input(f'Lista di numeri: ').split()]
    
    return lista_corrente


lista = inserendo_lista()
print(f'La lista inserita è: {lista}')

if 0 not in lista:
    print('Nella lista inserita non ci sono cifre 0!')
else:
    lista_transformata = spostare_zero(lista)
    print(f'La nuova lista e: {lista_transformata}')
