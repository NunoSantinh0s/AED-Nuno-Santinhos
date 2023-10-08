def cria_lista():

    numeros_inseridos = input('Insira uma sequência de números separados por espaços: ')

    dividir_numeros = numeros_inseridos.split()

    numeros = []

    for numero_dividido in dividir_numeros:
        try:
            numero = int(numero_dividido)
            numeros.append(numero)
        except:
            print(f'O valor {numero_dividido} não é um número válido.')
    
    return numeros

def acrescenta_elemento(lista):
    try:
        numero_inserido = input('Insira um número para acrescentar à lista: ')

        numero = float(numero_inserido)

        if numero.is_integer():
            numero = int(numero)

        lista.append(numero)

        print(f'Lista atualizada: {lista}')
    except:
        print('Valor inválido.')

    return lista

def insere_elemento(lista):
    try:
        print(f'Lista atual: {lista}')

        tamanho_lista = len(lista)

        posicao = int(input(f'Insira a posição onde deseja introduzir o elemento (0 até {tamanho_lista}): '))
        valor = input('Insira o valor do elemento que quer colocar: ')

        numero = float(valor)

        if numero.is_integer():
            numero = int(numero)

        if posicao < 0 or posicao >len(lista):
            print('Posição inválida.')
        
        else:
            lista.insert(posicao, numero)
            print('Elemento inserido.')

        print(f'Lista atualizada: {lista}')
    except:
        print('Valor inválido.')

    return lista

def remove_de_indice(lista):
    try:
        print(f'Lista atual: {lista}')
        tamanho_lista = len(lista) - 1

        posicao = int(input(f'Insira a posição do elemento quer quer remover (0 até {tamanho_lista}): '))
        
        if posicao < 0 or posicao >= len(lista):
            print('Posição inválida.')

        else:
            elemento_removido = lista.pop(posicao)
            print(f"Elemento {elemento_removido} removido com sucesso.")
        
        print(f'Lista atualizada: {lista}')

    except:
        print('Valor inválido.')
    
    return lista

def remove_elemento(lista):
    try:
        print(f'Lista atual: {lista}')

        elemento = input('Insira o elemento que deseja remover: ')

        numero = float(elemento)

        if numero.is_integer():
            numero = int(numero)
        
        if numero in lista:
            lista.remove(numero)
            print(f'Elemento {numero} removido com sucesso.')
        else:
            print(f'O elemento {numero} não está na lista')
    
        print(f'Lista atualizada: {lista}')
    
    except:
        print('Valor inválido.')
    
    return lista
