from curses.ascii import isspace


A = input("digite algo: ")
print("O Tipo primitivo dessse valor é ", type(A))
print("Só tem espaços? ", A.isspace())
print("É um número? ", A.isnumeric())
print("É alfabético? ", A.isalpha())
print("É alfanumérico? ", A.isalnum())
print("Está em maiúsculas? ", A.isupper())
print("Está em minúsculas? ", A.islower())
print("Está capitalizada? ", A.istitle())