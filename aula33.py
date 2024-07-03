"""

Repetições 
while (enquanto)
irá executar uma ação enquanto uma condição for verdadeira 
loop infinito > quando não tem condição
"""
qtd_linhas = 50
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
      coluna = 1
      while coluna <= qtd_colunas:
            print(f'{linha=} {coluna=}')
            coluna += 1
      linha += 1


print('Acabou')