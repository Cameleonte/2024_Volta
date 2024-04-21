somma_mario = float(input('Inserisci la paghetta di Mario: '))

pastina = 1
panino = 1.5
numero_giorni_mangiare = 0
mangiato_pastina = 0
mangiato_panino = 0

if somma_mario <= 0:
    print('Mario è rimasto senza soldi!')
else:
    in_classe = False
    while True:
        if in_classe:
            break
        print(f'\nMario ha a disposizione {somma_mario:.2f} euro. Che cosa vuole fare?\n'
              f'Prendersi una pastina (1) da 1 euro\nPrendersi un panino (2) da 1.50 euro\nRitorna in classe (3)? ', end='')
        scelta_colazione = int(input())
        if scelta_colazione == 1 and somma_mario - pastina < 0:
            print('Non ha abbastanza soldi, scegli altro: ')
        elif scelta_colazione == 2 and somma_mario - panino < 0:
            print('Non ha abbastanza soldi, scegli altro: ')
        else:
            while True:
                if scelta_colazione == 1:
                    somma_mario -= pastina
                    numero_giorni_mangiare += 1
                    mangiato_pastina += 1
                    break
                if scelta_colazione == 3:
                    in_classe = True
                    print('Mario va in classe! Ciao!')
                    break
                elif scelta_colazione == 2:
                    somma_mario -= panino
                    numero_giorni_mangiare += 1
                    mangiato_panino += 1
                    break
                if scelta_colazione == 3:
                    print('Mario va in classe! Ciao!')
                    in_classe = True
                    break
                elif scelta_colazione == 3:
                    print('Mario va in classe! Ciao!')
                    break
                else:
                    print(f'Scelta sbagliata!')
                    break
print(f'\nMario ha mangiato {numero_giorni_mangiare} giorni.\nIn qui panini ha mangiato {mangiato_panino} giorni'
      f' e pastini ha mangiato {mangiato_pastina} giorni.')
