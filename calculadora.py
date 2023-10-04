from leitura_dados import leitura
from operacoes import aritemetica
from resultado import apresentacao

def menu():
    print('Escolha uma opção:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Fatorial')
    print('4 - Sair')

def main():
    while True:
        menu()

        opcao = leitura.ler_inteiro('Escolha uma opção: ')

        if opcao == 1:
            num1 = leitura.ler_inteiro('Insira o primeiro número: ')
            num2 = leitura.ler_inteiro('Insira o segundo número: ')
            resultado = aritemetica.soma(num1, num2)
            apresentacao.mostrar_resultado('Soma', resultado)

        elif opcao == 2:
            num1 = leitura.ler_inteiro('Insira o primeiro número: ')
            num2 = leitura.ler_inteiro('Insira o segundo número: ')
            resultado = aritemetica.subtracao(num1, num2)
            apresentacao.mostrar_resultado('Subtração', resultado)

        elif opcao == 3:
            num = leitura.ler_inteiro_positivo('Insira um número para calcular o fatorial: ')
            resultado = aritemetica.fatorial(num)
            apresentacao.mostrar_resultado('Fatorial', resultado)

        elif opcao == 4:
            break

        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()