'''Hipotenusa'''

from math import hypot
x = float(input("Comprimento do cateto oposto: "))
y = float(input("Comprimento do cateto adjacente: "))
hip = hypot(x, y)
print(f"Hipotenusa: {hip:.2f}")
