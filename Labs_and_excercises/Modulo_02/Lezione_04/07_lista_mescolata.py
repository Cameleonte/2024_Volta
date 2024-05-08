import random


def mescolare(lista, acc=0, risultato=None):
    if risultato is None:
        risultato = []
    if lista:
        if len(lista) == 1:
            risultato.append(lista.pop(0))
        else:
            index_casuale = random.randint(1, len(lista) - 1)
            risultato.append(lista.pop(index_casuale))
        acc += 1
        return mescolare(lista, acc, risultato)
    elif acc == len(risultato):
        return risultato


creare_lista = [x for x in input("Creare una lista di elementi divisi da spazio: ").split()]
print(f"La lista originale è: {', '.join(creare_lista)}")
risposta = mescolare(creare_lista)
print(f"La lista mescolata è: {', '.join(risposta)}")
