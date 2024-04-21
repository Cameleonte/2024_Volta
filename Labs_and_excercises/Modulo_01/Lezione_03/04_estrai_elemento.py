def creare_tuple():
    lista_corrente = []
    while True:
        inserimento = input('Inserisci un numero della tupla corrente: ')
        if inserimento == "Fatto!":
            tupla1 = tuple(lista_corrente)
            break
        lista_corrente.append(inserimento)
        
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

indice = int(input("Inserisci l'indice per quale vuoi conoscere la cifra: "))
print(f'La cifra per l\'indice indicato è: {tupla_finale[indice]}')
