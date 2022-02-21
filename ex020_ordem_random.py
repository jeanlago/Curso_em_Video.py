'''gerar número aleatório'''

from random import shuffle
NOME1 = str(input("Digite um nome: "))
NOME2 = str(input("Digite um nome: "))
NOME3 = str(input("Digite um nome: "))
NOME4 = str(input("Digite um nome: "))

lista = [NOME1, NOME2, NOME3, NOME4]

shuffle(lista)
print(f"(A ordem é: {lista}")
