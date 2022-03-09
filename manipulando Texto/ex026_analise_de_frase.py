'''ler frase'''

FRASE = str(input("Digite uma frase: "))
FRASE = FRASE.strip()
FRASE = FRASE.upper()
print()
print(f"A letra 'A' apareceu {FRASE.count('A')} vezes,",end=' ')
print(f"apareceu pela primeira vez na posição {FRASE.find('A')+1} e ",end=' ')
print(f"pela última vez apareceu na posição {FRASE.rfind('A')+1}")
