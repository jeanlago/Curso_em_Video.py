'''testar se a cidade começa ou não com (santo)'''

CIDADE = str(input("Digite o nome da cidade: "))
LISTA = CIDADE.split()
print('Santo' in LISTA[0])
