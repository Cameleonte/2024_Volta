entrata = input('Inserisci un numero reale o uno immaginario: ')
if entrata.isdigit():
    entrata = int(entrata)
    print(f'Hai inserito il numero reale {entrata}.')
elif entrata.startswith('i'):
    entrata_lista = [x for x in entrata if x.isdigit()]
    entrata = ''.join(entrata_lista)
    if entrata.count('i') == 1 and entrata and entrata[0] == 'i':
        print(f'Hai inserito il numero immaginario {entrata}.')
    else:
        print('Ti manca il numero dietro la "i"!')
else:
    print('Inserisci un numero reale o un numero immaginario che inizia con la "i"')
