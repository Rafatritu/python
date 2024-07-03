"""
Iterando strings com while
"""

nome = 'Rafael'

tamanho_nome = len(nome)
nova_string = ''
i = 0

while i < tamanho_nome:
    nova_string += nome[i]
    if i < tamanho_nome - 1:  # Adiciona asterisco apenas entre as letras, não no final
        nova_string += '*'
    i += 1

print(nova_string)
 
