# Primeiro Projeto - Disciplina : Introdução a Programação - Calculadora Simples

import sys

nome = input('Digite seu nome: ')

print('Seja bem-vindo(a), {}, nosso objetivo é te ajudar a realizar operações matématicas'.format(nome.strip()))

continuar = input('Você deseja continuar? (Responda Sim ou Não?)')

if str(continuar).lower().strip() == 'sim':
    operacao = input('''
    Digite a operação matemática que vc deseja concluir:
    + adição
    - subtração
    * multiplicação
    / divisão
    ''')
    operacoes = ['+', '-', '*', '/']

    if operacao not in operacoes:
        print('Você não digitou um operador válido, execute o programa novamente.')
        sys.exit()

    num_1 = int(input('Digite seu primeiro número:'))
    num_2 = int(input('Digite seu segundo número:'))

    # adição
    if operacao == '+':
        print('{} + {} = {}'.format(num_1, num_2, (num_1 + num_2)))

    # subtração
    elif operacao == '-':
        print('{} - {} = {}'.format(num_1, num_2, (num_1 - num_2)))

    # miltiplicação
    elif operacao == '*':
        print('{} * {} = {}'.format(num_1, num_2, (num_1 * num_2)))

    # divisão
    elif operacao == '/':
        print('{} / {} = {}'.format(num_1, num_2, (num_1 / num_2)))

    print('Muito obrigada, volte quando precisar! Espero te ver em breve')



