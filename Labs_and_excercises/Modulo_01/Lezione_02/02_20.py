import random

print('************** Questo è "Ippodromo Capannelle" di Roma! *****************\n\n'
      'Quì puoi provare la tua fortuna e tornare a casa o andare alle Maldive!!!')
somma_iniziale = 100
auto_puntata = 5
if somma_iniziale <= 0:
    print('Sei rimasto a tasche vuote!\nSe vuoi puntare caccia fuori i soldi!')

else:
    print(f'\nHai a disposizione {somma_iniziale} euro. Scegli tra:\nAuto_puntata da 5 euro (1)\nDetermina la somma '
          'autonomamente (2)\nDecidi di ritirarti (3): ', end='')
    scelta_azione = int(input())

    while scelta_azione != range(1, 4):
        if scelta_azione == 1:
            print(f'Hai scelto auto_puntata da 5 euro.\nHai a disposizione {somma_iniziale} euro. '
                  f'Scegli puntata sul piazzato (P), vincente (V) o uscita (U): ', end='')
            scelta_puntare = input()
            scelta = False

            while True:
                if scelta_puntare == 'P':
                    somma_iniziale -= auto_puntata
                    scelta = True
                    primi_tre_in_classifica = ''
                    for cavallo in range(1, 4):
                        cavallo_classificato = random.randint(1, 10)
                        primi_tre_in_classifica += cavallo_classificato
                    numero_cavallo_puntato = random.randint(1, 10)
                    if str(numero_cavallo_puntato) in primi_tre_in_classifica:

                        somma_vinta = 2 * 5
                        somma_iniziale += somma_vinta
                        print(f'##### CONGRATULAZIONI! #####\nIl cavallo su qui hai puntato ha vinto!\n'
                              f'Ti sei guadagnato {somma_vinta} euro!')
                    else:
                        print('Purtroppo il cavallo su qui hai puntato non ha vinto questa volta!\n'
                              'Prova di nuovo la tua fortuna!')
                    break
                elif scelta_puntare == 'V':
                    somma_iniziale -= auto_puntata
                    scelta = True
                    numero_causale = random.randint(1, 10)
                    if numero_causale == 1:
                        somma_vinta = 5 * 5
                        somma_iniziale += somma_vinta
                        print(f'##### CONGRATULAZIONI! #####\nIl cavallo su qui hai puntato ha vinto!\n'
                              f'Ti sei guadagnato {somma_vinta} euro!')

                    else:
                        print('Purtroppo il cavallo su qui hai puntato non ha vinto questa volta!\n'
                              f'Prova di nuovo la tua fortuna!\nHai a disposizione {somma_iniziale} euro.')
                    break

                elif scelta_puntare == 'U':
                    scelta_azione = ''
                    break

                else:
                    print('Prova di nuovo: ', end='')
                    print(f'\nHai a disposizione {somma_iniziale} euro. Scegli tra:\nAuto_puntata da 5 euro (1)\n'
                          f'Determina la somma autonomamente (2)\nDecidi di ritirarti (3): ', end='')
                    scelta_puntare = input()

        elif scelta_azione == 2:
            puntata_giocatore = int(input('Inserisci il valore da puntare: '))
            print(f'Hai scelto di puntare {puntata_giocatore} euro.\nHai a disposizione {somma_iniziale} euro.'
                  f'Scegli puntata sul piazzato (P), vincente (V) o uscita (U): ', end='')
            scelta_puntare = input()
            scelta_valida = False

            while True:
                if scelta_valida:
                    break
                if scelta_puntare == 'P':
                    somma_iniziale -= puntata_giocatore
                    scelta_valida = True
                    numero_causale = random.randint(1, 10)
                    if numero_causale in range(1, 4):
                        somma_vinta = 2 * puntata_giocatore
                        somma_iniziale += somma_vinta
                        print(f'##### CONGRATULAZIONI! #####\nIl cavallo su qui hai puntato ha vinto!\n'
                              f'Ti sei guadagnato {somma_vinta} euro!')

                    else:
                        print('Purtroppo il cavallo su qui hai puntato non ha vinto questa volta!\n'
                              f'Prova di nuovo la tua fortuna!\nHai a disposizione {somma_iniziale} euro.')

                elif scelta_puntare == 'V':
                    somma_iniziale -= puntata_giocatore
                    scelta_valida = True
                    numero_causale = random.randint(1, 10)
                    if numero_causale == 1:
                        somma_vinta = 5 * puntata_giocatore
                        somma_iniziale += somma_vinta
                        print(f'##### CONGRATULAZIONI! #####\nIl cavallo su qui hai puntato ha vinto!\n'
                              f'Ti sei guadagnato {somma_vinta} euro!')

                    else:
                        print('Purtroppo il cavallo su qui hai puntato non ha vinto questa volta!\n'
                              'Prova di nuovo la tua fortuna!')

                elif scelta_puntare == 'U':
                    break

                else:
                    print('La scelta non è valida! Prova di nuovo: ', end='')
                    print(f'\nHai a disposizione {somma_iniziale} euro. Scegli tra:\nAuto_puntata da 5 euro (1)\n'
                          f'Determina la somma autonomamente (2)\nDecidi di ritirarti (3): ', end='')
                    scelta_puntare = input()

        elif scelta_azione == 3:
            print(f'Hai fatto la scelta giusta! Metti in tasca i tuoi {somma_iniziale} euro! Ci rivedremo, a presto!')
            break

        else:
            print('Inserisci un numero tra 1, 2 e 3: ', end='')
            print(f'\nHai a disposizione {somma_iniziale} euro. Scegli tra:\nAuto_puntata da 5 euro (1)\n'
                  f'Determina la somma autonomamente (2)\nDecidi di ritirarti (3): ', end='')
            scelta_azione = int(input())
