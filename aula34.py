frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

i = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
     letra_atual = frase[i]
     quantas_vezes_apareceu_letra = frase.count(letra_atual)
     if letra_atual == ' ':
          i += 1
          continue
     if qtd_apareceu_mais_vezes < quantas_vezes_apareceu_letra:
          qtd_apareceu_mais_vezes = quantas_vezes_apareceu_letra
          letra_apareceu_mais_vezes = letra_atual
     print(letra_atual, quantas_vezes_apareceu_letra)
     i += 1

print('A letra que mais apareceu foi '
      f'{letra_apareceu_mais_vezes}, que apareceu'
      f' {qtd_apareceu_mais_vezes} vezes' 
)   