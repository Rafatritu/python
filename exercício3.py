primeiro_valor = input("Digite o primeiro valor:")
segundo_valor = input("Digite o segundo valor:")
maior = primeiro_valor > segundo_valor
maior_2 = segundo_valor > primeiro_valor
if maior:
    print("O maior valor é:", primeiro_valor)

elif maior_2:
    print("O maior valor é:", segundo_valor)

else:
    print("Ambos são iguais, não executaremos o resultado")
