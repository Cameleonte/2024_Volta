"""def costruire_set(insieme_corrente):
    while True:
        elemento = input('Inserisci un simbolo dell insieme: ')
        insieme_corrente.add(elemento)
        insieme_finito = input('Hai completato l\'insieme corrente? (si/no) ')
        if insieme_finito == 'si':
            break
    return insieme_corrente


print('Costruisci un insieme! ')

insieme = set()
insieme_finale = costruire_set(insieme)
print(f'L\'insieme ottenuto è: {insieme_finale}')

elemento_casuale = input('Inserisci l\'elemento per controllare se presente: ')
if elemento_casuale in insieme_finale:
    print(True)
else:
    print(False)
"""

def costruire_set(insieme_corrente):
    while True:
        elemento = input('Inserisci un simbolo dell insieme: ')
        if elemento == "Fatto!":
            break
        insieme_corrente.add(elemento)
    return insieme_corrente


print('Costruisci un insieme! ')
print('Per poter chiudere l\'insieme corrente scrivi: Fatto!')
insieme = set()
insieme_finale = costruire_set(insieme)
print(f'L\'insieme ottenuto è: {insieme_finale}')

elemento_casuale = input('Inserisci l\'elemento per controllare se presente: ')
if elemento_casuale in insieme_finale:
    print(True)
else:
    print(False)