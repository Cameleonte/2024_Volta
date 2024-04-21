numero_casuale = int(input('Inserisci un numero per quali vuoi calcolare la somma dei primi numeri pari: '))

somma_pari = 0

for num in range(1, numero_casuale + 1):
    if num % 2 == 0:
        somma_pari += num
print(somma_pari)
