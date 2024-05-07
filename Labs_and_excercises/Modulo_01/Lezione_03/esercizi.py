def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


num = 7

for numero in range(1, num + 1):
    risultato = fibonacci(numero)
    print(risultato, end=' ')

#print("Il numero fibonacci al posto", num, "è:", risultato)
