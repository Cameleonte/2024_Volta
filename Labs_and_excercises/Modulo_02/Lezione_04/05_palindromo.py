def controllo(frase, cons=False, acc=0, dis=-1):
    if acc >= len(frase):
        return cons
    if frase[acc] == frase[dis]:
        acc += 1
        dis -= 1
        cons = True
        return controllo(frase, cons, acc, dis)
    else:
        cons = False
        return


stringa = input('Inserisci una stringa: ')
conferma = controllo(stringa)
if conferma:
    print('La stringa è un palindromo.')
else:
    print('La stringa non è un palindromo.')
