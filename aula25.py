"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Eu irei dobrar o número que você digitar: ')

try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número')   
# if numero_str.isdigit():
#     numero_float = float(numero)
#     print(f'O dobro de {numero} é {numero_float * 2:.2f}')
# else:
     

