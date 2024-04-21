numero = int(input('Inserire un numero: '))

moltiplicatore = 1
print(f'La tabella del {numero} è:')

while moltiplicatore <= numero:
    risultato = moltiplicatore * numero
    tabella = f'{moltiplicatore} * {numero} = {risultato}'
    moltiplicatore += 1

    print(f'{tabella}')
