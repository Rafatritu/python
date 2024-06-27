condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Você digitou: {nome}')

    if nome.lower() == 'sair':
        print('Saindo do loop...')
        break

print('Acabou')
