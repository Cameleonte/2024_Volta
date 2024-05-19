import random

try:
    numeratore = int(input('Inserisci un numero qualsiasi: '))
    denominatore_casuale = random.randrange(4)
    print(f'Il denominatore generato casualmente è: {denominatore_casuale}')
    risultato = numeratore / denominatore_casuale

except ZeroDivisionError:
    print('Errore: \nIl denominatore generato è 0.\nDivisione per zero non consentita.')

except ValueError:
    print('Inserisci un valore numerico valido.')
    
else:
    print(f'Il risultato è: {risultato}')

finally:
    print('\nOperazione conclusa.')