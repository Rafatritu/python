# 1 QUESTÃO
#numero_str = input("Digite um número: ")

# Converta a entrada para um número inteiro
#numero = int(numero_str)

#if numero % 2 == 0:
#    print('Esse número é par')
#elif numero % 2 == 1:
#    print('Ímpar')
#else:
#   print('Você não digitou um número válido') "ERA PRA TER UTILIZADO UM IS.DIGIT OU TRY E EXPECT"   

# 2 QUESTÃO 
#entrada = input('Digite a hora em números inteiros: ')

#try:
#    hora = int(entrada)

#    if hora >= 0 and hora <= 11:
#        print('Bom dia')
#    elif hora >= 12 and hora <= 17:
#        print('Bom tarde')
#    elif hora >= 18 and hora <= 23:
#        print('Bom noite')
#    else:
#        print('Não conheço essa hora')
#except:
#    print('Por favor, digite apenas números inteiros')


nome = input('Escreva seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal') 

else:
    print('Seu nome é grande')    
       