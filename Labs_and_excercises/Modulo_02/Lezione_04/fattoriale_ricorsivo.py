def fattoriale_ricorsivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fattoriale_ricorsivo(n - 1)


print(fattoriale_ricorsivo(5))
