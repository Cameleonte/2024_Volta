dizionario = {}

print('Costruisci un dizionario!')
print('Per poter chiudere il dizionario corrente scrivi: Fatto!')
while True:
    chiave = input('Inserisci la chiave: ')
    if chiave == "Fatto!":
        break
    valore = input('Inserisci il valore: ')
    if not dizionario:
        dizionario[chiave] = ''
    dizionario.update({chiave: valore})

lunghezza_dizionario = len(dizionario)
print(f'La lunghezza del dizionario ottenuto è: {lunghezza_dizionario}')
