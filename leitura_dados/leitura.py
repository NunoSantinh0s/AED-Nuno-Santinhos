def ler_inteiro(numero):
    try:
        return int(input(numero))

    except ValueError:
        print('Insira um número inteiro válido.')
        return ler_inteiro(numero)
    

def ler_inteiro_positivo(numero):
    valor = ler_inteiro(numero)
    while valor<= 0:
        print('Insira um número inteiro positivo.')
        valor = ler_inteiro(numero)
    
    return valor