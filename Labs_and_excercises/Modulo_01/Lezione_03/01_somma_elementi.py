def somma_elementi(lista_numeri):
	risultato = sum(lista_numeri)
	return risultato


numeri = [float(x) for x in input('Inserisci una lista di numeri: ').split()]

risultato_finale = somma_elementi(numeri)
print(f'La somma degli elementi e: {risultato_finale:.3f}')
