def maximo(lista):
    if len(lista) == 0:
        print('A lista está vazia. Não existe o máximo.')
        return None
    
    max_elemento = lista[0]

    for elemento in lista:
        if elemento > max_elemento:
            max_elemento = elemento

    print(f'Maior elemento da lista: {max_elemento}')
    
    return lista

def posicao_maximo(lista):
    if len(lista) == 0:
        print('A lista está vazia. Não existe a posição do máximo.')
        return None
    
    max_elemento = lista[0]
    posicao = 0

    for i, elemento in enumerate(lista):
        if elemento > max_elemento:
            max_elemento = elemento
            posicao = i
    
    print(f'A posição do maior elemento na lista é: {posicao}')

    return lista

def soma(lista):
    
    soma_total = 0

    for elemento in lista:
        soma_total += elemento

    print(f'A soma total dos elementos da lista é: {soma_total}')

    return lista

def media(lista):
    if len(lista) == 0:
        print('A lista está vazia. Não é possível calcular a média.')
        return

    soma_total = 0

    for elemento in lista:
        soma_total += elemento

    media = soma_total / len(lista)

    print(f'A média dos elementos da lista é: {media}')

    return lista
