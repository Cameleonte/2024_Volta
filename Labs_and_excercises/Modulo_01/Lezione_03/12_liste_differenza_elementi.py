def differenza_elementi(lista_a):
    lista_differenze = []
    for lista_corrente in lista_a:
        valore_max = max(lista_corrente)
        valore_min = min(lista_corrente)
        differenza = valore_max - valore_min
        lista_differenze.append(differenza)
    return lista_differenze


def inserendo_liste():
    lista_principale = []
    num = 1
    print(f'Inserire due liste da almeno 2 numeri divisi solo da uno spazio.')
    while True:
        if num == 3:
            break
        lista_corrente = [int(x) for x in input(f'Lista {num}: ').split()]
        if len(lista_corrente) <= 1:
            print("Gli elementi nella lista devono essere almeno 2!")
        else:
            lista_principale.append(lista_corrente)
            num += 1
    return lista_principale


lista = inserendo_liste()
print('\nLe liste inserite sono: ')
for lst in lista:
    print(f'{lst}')
    
diff = differenza_elementi(lista)
for element in diff:
    if element == diff[0]:
        print(f"La differenza tra il massimo ed il minimo valore nella prima lista è: {element}")
    else:
        print(f"Quella nella seconda è: {element}")
