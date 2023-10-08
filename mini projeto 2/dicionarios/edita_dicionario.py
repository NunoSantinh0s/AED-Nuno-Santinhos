def cria_dicionario():
    entrada = input('Introduza uma sequência de pares chave valor, separados por vírgula e ":" (exemplo: Filipe:14, Antonio:23, Ines:19): ')

    elementos = entrada.split(',')

    dic = {}

    for elemento in elementos:
        chave, valor = elemento.split(':')
        dic[chave.strip()] = int(valor.strip())

    print(f'Dicionário criado: {dic}')

    return dic

def insere_elemento(dicionario):
    chave = input('Introduza a chave que deseja inserir: ')
    valor = input('Introduza o valor correspondente à chave: ')

    dicionario[chave] = valor

    print(f'Dicionário atualizado: {dicionario}')

    return dicionario

def remove_elemento(dicionario):
    print(f'Dicionario atual: {dicionario}')
    chave = input('Introduza a chave que deseja remover: ')

    if chave in dicionario:
        del dicionario[chave]
        print(f'A chave {chave} foi removida.')

    else:
        print(f'A chave {chave} não foi encontrada.')
    
    print(f'Dicionário atualizado: {dicionario}')
    
    return dicionario

