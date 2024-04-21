number1 = int(input('Inserisci il primo numero: '))
number2 = int(input('Inserisci il secondo numero: '))
number3 = int(input('Inserisci il terzo numero: '))

if number1 < number2 and number1 < number3:
	print(f'Il terzo numero {number3} è il massimo fra i tre numeri inseriti.')
if number2 < number1 < number3:
	print(f'Il terzo numero {number3} è il massimo fra i tre numeri inseriti.')
elif number1 < number2 and number2 > number3:
	print(f'Il secondo numero {number2} è il massimo fra i tre numeri inseriti.')
elif number1 > number2 > number3:
	print(f'Il secondo numero {number2} è il massimo fra i tre numeri inseriti.')
elif number1 > number2 and number1 > number3:
	print(f'Il primo numero {number1} è il massimo fra i tre numeri inseriti.')
elif number2 > number1 > number3:
	print(f'Il primo numero {number1} è il massimo fra i tre numeri inseriti.')
