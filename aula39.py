for i in range (10):
    if i == 2:
        print('Irei pular esse 2 viu')
        continue

    if i == 8:
        print('Aqui a gente para')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For executado!!')        
