stringa = input('Inserisci una parola: ')

vocali = 'aoeiu'
stringa_senza_vocali = '' 

for letter in stringa:
	if letter not in vocali:
		stringa_senza_vocali += letter
print(f'La nuova stringa senza vocali è "{stringa_senza_vocali}".')
