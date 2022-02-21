'''Calcular desconto.'''

precoInicial = float(input("Qual o preço do produto? "))
desconto = int(input("Qual a % de desconto?"))
precoFinal = (precoInicial/100)*desconto
print(f"Você terá R${precoFinal} de desconto.")
