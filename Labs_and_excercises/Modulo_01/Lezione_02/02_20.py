import random


def main_func(somma_corrente, chiusura):

    if somma_corrente <= 0:
        print('Sei rimasto senza denaro quindi non poi più puntare!\nArrivederci!')
        chiusura = True
        return somma_corrente, chiusura

    else:
        print(f'\nHai a disposizione {somma_corrente} euro. Scegli tra:\nAuto-puntata da 5 euro (1)\n'
              f'Determina la somma da puntare autonomamente (2)\nDecidi di ritirarti (3): ', end='')

        return somma_corrente, chiusura


def scegliere_azione(somma_avanzata):
    scelta_azione = int(input())
    while scelta_azione in range(1, 4):
        if scelta_azione == 1:
            auto_puntata = 5
            print(f'Hai scelto Auto-puntata da 5 euro.\nHai a disposizione {somma_avanzata} euro. '
                  f'Scegli puntata sul piazzato (P), vincente (V) o uscita (U): ', end='')

            return somma_avanzata, auto_puntata

        elif scelta_azione == 2:
            puntata_giocatore = int(input('Inserisci il valore da puntare: '))
            if puntata_giocatore > somma_avanzata:
                print('La somma scelta e più alta a quella che hai a disposizione! Scegli di nuovo: ')
                scegliere_azione(somma_avanzata)
            else:
                print(f'Hai scelto di puntare {puntata_giocatore} euro.\nHai a disposizione {somma_avanzata} euro. '
                      f'Scegli puntata sul piazzato (P), vincente (V) o uscita (U): ', end='')

            return somma_avanzata, puntata_giocatore

        elif scelta_azione == 3:
            print(f'\nHai fatto la scelta giusta! Metti in tasca i tuoi {somma_avanzata} euro! Ci rivedremo, a presto!')

            return somma_avanzata, 0

    else:
        print('Inserisci un numero tra 1, 2 e 3: ', end='')
        scegliere_azione(somma_avanzata)


def scegliere_puntare(somma, somma_puntata, scelta_uscita):
    scelta_puntare = input()
    while True:
        if scelta_puntare == 'P':
            somma -= somma_puntata
            numero_cavallo_auto_puntato = random.randint(1, 10)
            print(f"Il cavallo su qui hai puntato ha il numero {numero_cavallo_auto_puntato}")
            primi_tre_in_classifica = {}
            print('I primi 3 cavalli classificati sono: ')
            posto = 1
            while posto < 4:
                numero_cavallo = random.randint(1, 10)
                if numero_cavallo in primi_tre_in_classifica.values():
                    continue
                primi_tre_in_classifica[posto] = numero_cavallo
                print(f'{posto} posto: Cavallo numero {numero_cavallo}')
                posto += 1
            if numero_cavallo_auto_puntato in primi_tre_in_classifica.values():
                somma_vinta = 2 * somma_puntata
                somma += somma_vinta
                print(f'##### CONGRATULAZIONI! #####\n        HAI VINTO!\n'
                      f'Hai guadagnato {somma_vinta} euro!')
            else:
                print('Purtroppo non hai vinto questa volta!\n'
                      'Prova di nuovo la tua fortuna!')
            return somma, somma_puntata, scelta_uscita

        elif scelta_puntare == 'V':
            somma -= somma_puntata
            print("Scegli il numero del cavallo su qui vuoi puntare (da 1 a 10): ", end='')
            cavallo_puntato = int(input())
            cavallo_vincente = random.randint(1, 10)
            if cavallo_vincente == cavallo_puntato:
                somma_vinta = 5 * somma_puntata
                somma += somma_vinta
                print(f'##### CONGRATULAZIONI! #####\nIl cavallo su qui hai puntato ha vinto!\n'
                      f'Ti sei guadagnato {somma_vinta} euro!')

            else:
                print(f'Il cavallo vincente è numero {cavallo_vincente}. Purtroppo il cavallo su qui hai puntato '
                      f'non ha vinto questa volta!\nProva di nuovo la tua fortuna!')
            return somma, somma_puntata, scelta_uscita

        elif scelta_puntare == 'U':
            print("\nHai scelto di uscire dal gioco. Buona fortuna! Arrivederci.")
            scelta_uscita = True
            return scelta_uscita

        else:
            print('Prova di nuovo: ', end='')
            scegliere_puntare(somma, somma_puntata, scelta_uscita)


print('\n***** Questo è "Ippodromo Capannelle" di Roma! *****')

puntata = 0
uscita = False
somma_iniziale = 100
while not uscita:
    if not uscita:
        somma_iniziale, uscita = main_func(somma_iniziale, uscita)
    if not uscita:
        somma_iniziale, puntata = scegliere_azione(somma_iniziale)
    if not uscita:
        somma_iniziale, puntata, uscita = scegliere_puntare(somma_iniziale, puntata, uscita)
