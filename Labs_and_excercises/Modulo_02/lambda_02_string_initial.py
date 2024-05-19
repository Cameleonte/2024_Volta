stringa = input('Inserisci una stringa: ')
simbolo = input('Inserisci il simbolo che vuoi controllare: ')
ris = ''

a = lambda x: True if stringa.startswith(x) else False
ris = 'Vero' if a == True else 'Falso'

print(f"La stringa '{stringa}' comincia con il simbolo '{simbolo}': {ris}")
