'''fazer a tabuada de um número.'''

N = int(input("Digite um número: "))
for i in range (0, 11):
    soma = N * i
    print(f"{N} * {i} = {soma}")
