'''Calcular novo salário'''

salario = float(input("Digite o seu salário: "))
aumento = (salario / 100) * 15
salario = salario + aumento
print(f"Novo salário = R${salario}")
