from listas import edita_lista, transforma_lista, operacoes_lista
from dicionarios import edita_dicionario, transforma_dicionario

def menu_listas():
    minha_lista = []

    while True:
        print('Menu:')
        print('1 - Criar uma lista')
        print('2 - Acrescentar um elemento')
        print('3 - Inserir elemento por índice')
        print('4 - Remover elemento por índice')
        print('5 - Remover elemento por valor')
        print('6 - Ordenar lista')
        print('7 - Encontrar o maior elemento')
        print('8 - Encontrar a posição do maior elemento')
        print('9 - Calcular a soma dos elementos')
        print('10 - Calcular a média dos elementos')
        print('0 - Sair')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            minha_lista = edita_lista.cria_lista()
        elif escolha == 2:
            minha_lista = edita_lista.acrescenta_elemento(minha_lista)
        elif escolha == 3:
            minha_lista = edita_lista.insere_elemento(minha_lista)
        elif escolha == 4:
            minha_lista = edita_lista.remove_de_indice(minha_lista)
        elif escolha == 5:
            minha_lista = edita_lista.remove_elemento(minha_lista)
        elif escolha == 6:
            minha_lista = transforma_lista.ordena(minha_lista)
        elif escolha == 7:
            operacoes_lista.maximo(minha_lista)
        elif escolha == 8:
            operacoes_lista.posicao_maximo(minha_lista)
        elif escolha == 9:
            operacoes_lista.soma(minha_lista)
        elif escolha == 10:
            operacoes_lista.media(minha_lista)
        elif escolha == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_dicionarios():
    meu_dicionario = {}
    while True:
        print('Menu Dicionários:')
        print('1 - Criar um dicionário')
        print('2 - Inserir elemento')
        print('3 - Remover elemento')
        print('4 - Apresentar dicionário ordenado')
        print('5 - Calcular a soma dos valores')
        print('6 - Calcular a média dos valores')
        print('7 - Encontrar o par chave:valor com maior valor')
        print('0 -  Sair do Menu Dicionários')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            meu_dicionario = edita_dicionario.cria_dicionario()
        elif escolha == 2:
            meu_dicionario = edita_dicionario.insere_elemento(meu_dicionario)
        elif escolha == 3:
            meu_dicionario = edita_dicionario.remove_elemento(meu_dicionario)
        elif escolha == 4:
            transforma_dicionario.apresenta_ordenado(meu_dicionario)
        elif escolha == 5:
            transforma_dicionario.soma_valores(meu_dicionario)
        elif escolha == 6:
            transforma_dicionario.media_valores(meu_dicionario)
        elif escolha == 7:
            transforma_dicionario.maximo_valor(meu_dicionario)
        elif escolha == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        print('Menu Principal:')
        print('1 - Operações com Listas')
        print('2 - Operações com Dicionários')
        print('0 - Sair')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            menu_listas()
        elif escolha == 2:
            menu_dicionarios()
        elif escolha == 0:
            break
        else:
            print('Opção inválida. Tente outra vez.')  
    

if __name__ == "__main__":
    main()