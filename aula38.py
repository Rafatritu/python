"""

          (FOR DEBAIXO DOS PANOS)
Iterável -> str, range etc.
Iterador -> quem vai saber entregar um valor por vez
next -> me entregue o próximo valor
iter - me entregue seu iterador
"""

texto ='Rafa' #iterável
iterador = iter(texto) #iterator

while True:
    try:
        letra = next (iterador)
        print(letra)
    except StopIteration:
        break    

