def ordena(lista):
    try:
        ordem = int(input('Deseja ordenar a lista em ordem crescente(1) ou decrescente(2): '))

        if ordem == 1:
            lista.sort()
            print('Lista ordenada em ordem crescente.')
            print(f'Lista: {lista}')
        
        elif ordem == 2:
            lista.sort(reverse=True)
            print('Lista ordenada em ordem decrescente.')
            print(f'Lista: {lista}')

        
        else:
            print('Escolha inválida.')
        
        return lista
        
    except:
        print('Valor inválido')
        return None
