"""
Calculadora com While
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Escolha a operação: (+-/*): ')
    numeros_validos = False

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except ValueError:
        numeros_validos = False

    if not numeros_validos:
        print('Erro! Números inválidos.')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador errado')
        continue

    if len(operador) > 1:
        print('Não pode mais de um operador!!')
        continue

    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)   

    elif operador == '*':
        print(num_1_float * num_2_float)

    elif operador == '/':
        print(num_1_float / num_1_float)   

    else:
        print('Erro novamente!!')         
    
    sair = input('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break