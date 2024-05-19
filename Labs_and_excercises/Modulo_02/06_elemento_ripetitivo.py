def controllo_ripetizioni(lista, elem, contatore=0):
    for index in range(len(lista)):
        if elem == lista[index]:
            contatore += 1
            lista.pop(index)
            return controllo_ripetizioni(lista, elem, contatore)
    return contatore


lista_elementi = [x for x in input('Inserisci una lista di elementi divisi solo da uno spazio: ').split()]
elemento = input('Inserisci un elemento che vuoi controllare se si trova nella lista: ')

cont = controllo_ripetizioni(lista_elementi, elemento)
print(f'L\'elemento \'{elemento}\' compare {cont} volte nella lista.')
