'''gerar número aleatório'''

import random
vet : str = [0 for x in range(4)]
for i in range (4):
    vet[i] = str(input(f"{i+1}º aluno: "))
def select_random(alunos):
    """essa funcao escolhe um nome aleatorio dentre os vet."""
    return random.choice(alunos)

print(f"{select_random(vet)}")
