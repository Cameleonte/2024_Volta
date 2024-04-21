def creare_tuple():
    corrente_lista = []
    while True:
        cifra = input('Inserisci un numero della tupla corrente: ')
        if cifra == "Fatto!":
            tupla1 = tuple(corrente_lista)
            break
        corrente_lista.append(int(cifra))
                        
    return tupla1


def funzione_principale():
    tupla = ()
    while True:
        tupla_corrente = creare_tuple()
        tupla += tupla_corrente
        print(f'La tupla corrente è: {tupla_corrente}')
        risposta_finale = input('Hai concluso con le tuple? (si/no) ')
        if risposta_finale == 'si':
            break
    
    return tupla

print('Costruisci una tupla! Per poter concludere con le tupla scrivi: "Fatto!"')
tupla_finale = funzione_principale()

print(f'La tupla finale è: {tupla_finale}')
