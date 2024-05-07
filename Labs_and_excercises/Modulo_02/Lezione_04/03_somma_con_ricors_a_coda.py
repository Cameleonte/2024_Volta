import functools


@functools.lru_cache(maxsize=None)
def somma(cifra, acc=0, cont=0):
    if cont == cifra:
        return acc
    else:
        cont += 1
        acc += cont
        return somma(cifra, acc, cont)


numero = int(input('Inserisci un numero fino a quale vuoi calcolare la somma: '))
risultato = somma(numero)
print(f'La somma dei primi {numero} numeri interi è: {risultato}')
