'''angulo'''

from math import acos, asin, atan
x = int(input("Digite um angulo: "))
sen = asin(x)
cos = acos(x)
tan = atan(x)
print(f"Seno = {sen}, cosseno = {cos} e tangente = {tan}")
