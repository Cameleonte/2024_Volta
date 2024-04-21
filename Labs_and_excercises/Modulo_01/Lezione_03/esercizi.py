def fattoriale(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)


num = 5
risultato = fattoriale(num)
print("Il fattoriale di", num, "è:", risultato)
