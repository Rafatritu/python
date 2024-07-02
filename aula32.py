"""

Reptições 
while (enquanto)
irá executar uma ação enquanto uma condição for verdadeira 
loop infinito > quando não tem condição
"""

contador = 0
while contador <= 100:
    contador += 1

    if contador == 6:
        print("sem o 6")
        continue 

    if contador >= 10 and contador <= 27:
        print("sem o", contador)
        continue 

    print (contador)

    if contador == 40:
        break