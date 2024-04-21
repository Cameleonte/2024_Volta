def costruire_set(insieme_corrente):
    while True:
        elemento = input('Inserisci un simbolo dell insieme: ')
        if elemento == "Fatto!""
            break
        insieme_corrente.add(elemento)
        
    return insieme_corrente


print('Costruisci un insieme: ')
print('Per poter chiudere l\'insieme corrente scrivi: Fatto!')
insieme1 = set()
costruire_set(insieme1)

insieme2 = set()
costruire_set(insieme2)

intersezione = insieme1 & insieme2
print(f'L\'intersezione dei due insiemi è: {intersezione}')
