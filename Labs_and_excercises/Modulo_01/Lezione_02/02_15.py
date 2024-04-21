numero1 = int(input('Inserisci il primo numero: '))
numero2 = int(input('Inserisci il secondo numero: '))

num_primo = False
if numero1 == 2:
    print(2)

for numero_primo in range(numero1, numero2 + 1):
    if numero1 <= 1:
        print('Il primo numero che hai inserito non è valido, riprova.')
        break
    for divisore in range(2, numero_primo):
        if numero_primo % divisore == 0:
            num_primo = False
            break
        else:
            num_primo = True
    if num_primo:
        print(numero_primo)
