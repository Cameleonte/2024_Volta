from itertools import permutations

lista_elementi = [x for x in input('Inserisci una lista di elementi diversi '
                                   'uno dall\'altro divisi solo da uno spazio: ').split()]

permutazioni = permutations(lista_elementi)
nuova_lista = list(permutazioni)
# se ci sono elementi uguali nella prima lista si crea un insieme che cancella i risultati uguali
nuova_lista = set(nuova_lista)

for a in nuova_lista:
    print(a)
