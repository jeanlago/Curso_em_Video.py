'''Exercício 23'''

NAME = str(input("Digite seu nome: "))
#comando adicionar tudo maiúsculo.
print(f"seu nome em maiúscula: {NAME.upper()}")
#comando adicionar tudo minúsculo.
print(f"seu nome em minúscula: {NAME.lower()}")
#comando remover espaços e informar quantidade de caracteres.
print("seu nome tem ao todo {} números".format(len(NAME) - NAME.count(' ')))
#comando separar palavras em uma lista.
NAME = (NAME.split())
#comando mostrar palavra na posição 0 da lista.
print(f"Seu primeiro nome é: {len(NAME[0])}")
