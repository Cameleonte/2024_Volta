dizionario = {}

print('Costruisci il dizionario!')
print('Per poter chiudere il dizionario corrente scrivi: Fatto!')
while True:
    chiave = input('Inserisci la chiave: ')
    if chiave == "Fatto!":
        break
    valore = input('Inserisci il valore: ')
    if not dizionario:
        dizionario[chiave] = ''
    dizionario.update({chiave: valore})
    print(f"Il dizionario costruito per il momento e: {dizionario}")
    
chiave_cercata = input('Inserisci la chiave per quale vuoi conoscere il valore: ')
if dizionario[chiave_cercata]:
    valore_cercata = dizionario[chiave_cercata]
    print(f'Il valore associato alla chiave \'{chiave_cercata}\' e: {valore_cercata}')
else:
    print('Per questa chiave non c\'e nessun valore')
