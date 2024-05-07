def permutazioni(lista, acc):
    elemento = lista.pop()
    lista.insert(acc - 1, elemento)
    if acc == len(lista):
        print_list = ' '.join(lista)
        print(print_list)
        return
    else:
        acc += 1
        print_list = ' '.join(lista)
        print(print_list)
        permutazioni(lista, acc)


lista_elementi = [x for x in input('Inserisci una lista di elementi diversi '
                                   'uno dall\'altro divisi solo da uno spazio: ').split()]

for num in range(len(lista_elementi), 0, - 1):
    permutazioni(lista_elementi, num)
