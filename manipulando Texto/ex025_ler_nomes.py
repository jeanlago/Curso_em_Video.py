'''Ler nomes'''

NAME = str(input("Digite seu nome: "))
NAME = NAME.title()
if NAME.find('Silva') >= 0:
    print("Possui Silva no nome.")
else:
    print("Não possui Silva no nome:")
