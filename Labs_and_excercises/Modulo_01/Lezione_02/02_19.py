voto_teoria = float(input('Inserisci il voto di teoria: '))
voto_pratica = float(input('Inserisci il voto di pratica: '))

risultato_finale = voto_pratica + voto_teoria
if ((voto_teoria <= 0 and risultato_finale > 18) or 
        (voto_teoria <= 0 and voto_pratica < 18) or
        (voto_teoria > 0 and risultato_finale < 18)):
    print('Bocciato!')
elif 31 <= risultato_finale <= 32:
    print('Congratulazioni: 30 e lode')
else:
    print(f'Promosso! Il voto dell\'esame è {risultato_finale}')
