nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
tamanho_nome = len(nome)




if nome and idade:
    print("BEM VINDO!!")

    print(f'Seu nome é: {nome}')
    print("Seu nome ao contrário é:", nome[::-1])
    
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f'Seu nome possui {tamanho_nome} caracteres')

    print(f'Primeira letra: {nome [0]}')
    print(f'Sua última letra é: {nome [-1]}')
else:
    print("Você não digitou nada.")