import random


class MiaEccezione(Exception):
    def __init__(self, messaggio):
        self.messaggio = messaggio
        super().__init__(self.messaggio)


def istanza_lista():
    try:
        nuova_lista = [random.randrange(1, 100) for x in range(0, 5)]
        print(f"La lista generata casualmente è: {nuova_lista}")
        print(f'\nScrivi un numero che vuoi inserire dentro la lista: ', end='')
        a = int(input())
        print('Scegli la sua posizione tra 0 e 4 inclusi: ', end='')
        index = int(input())
        if index >= 5 or index < 0:
            raise MiaEccezione('Se vuoi inserire la cifra selezionata nella posizione specificata ella dev\'essere'
                               ' nell\'intervallo da 0 a 4.')
    except MiaEccezione as e:
        print("Attenzione!", e)
        print('Inserisci \n1 per riprovare\n2 per uscire: ', end='')
        if int(input()) == 1:
            istanza_lista()
        return

    else:
        nuova_lista.insert(index, a)
        print(f'La nuova lista è: {nuova_lista}')


istanza_lista()
