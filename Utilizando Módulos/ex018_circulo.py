'''angulo'''

import math
x = float(input("Digite um angulo: "))
sen = math.sin(math.radians(x))
cos = math.cos(math.radians(x))
tan = math.tan(math.radians(x))
print(f"Seno = {sen:.2f}, cosseno = {cos:.2f} e tangente = {tan:.2f}")
