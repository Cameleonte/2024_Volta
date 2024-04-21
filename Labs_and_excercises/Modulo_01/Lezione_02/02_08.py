stringa = input('Inserisci una parola: ')

vocali = 'aoeiu'
numero_vocali = 0 

for letter in stringa:
	if letter in vocali:
		numero_vocali += 1
print(f'I vocali nella stringa "{stringa}" sono {numero_vocali}.')
