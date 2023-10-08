def apresenta_ordenado(dicionario):
    for chave in sorted(dicionario.keys()):
        valor = dicionario[chave]
        print(f'Chave: {chave}, Valor: {valor}')

def soma_valores(dicionario):
    soma = 0
    for valor in dicionario.values():
        soma += valor

    resposta = print(f'A soma de todos os valores do dicionário é: {soma}')

    return resposta

def media_valores(dicionario):
    valores = list(dicionario.values())

    if not valores:
        print('O dicionário está vazio.')
        return None
    
    soma = sum(valores)
    media = soma / len(valores)

    resposta = print(f'A média de todos os valores do dicionario é: {media}') 

    return resposta

def maximo_valor(dicionario):
    if not dicionario:
        print('O dicionário está vazio.')
        return None
    
    chave_max = max(dicionario, key=dicionario.get)
    valor_max = dicionario[chave_max]

    resposta = print(f'Chave: {chave_max}, Valor: {valor_max}')

    return resposta
