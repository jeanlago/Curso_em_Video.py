'''Acima diagonal'''

N = int(input("Qual a ordem da matriz? "))
MAT: int = [[0 for x in range(N)] for x in range(N)]
for i in range(N):
    for j in range(N):
        MAT[i][j] = int(input(f"Elemento [{i}:{j}]: "))
SOMA = 0

for i in range(N):
    for j in range(N):
        if i < j:
            SOMA = SOMA + MAT[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {SOMA}")
