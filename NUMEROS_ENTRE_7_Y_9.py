# Programa para saber los multiplos de 7 y 9 que hay entre 1000 y 5000

import math 
contador7 = 0
contador9 = 0

for i in range(1000, 5001):
    if i % 7 == 0:
        contador7 = contador7 + 1

    if i % 9 == 0:
        contador9 = contador9 + 1

print("cantidad de multiplos de 7 encontrados en 1000 a 5000: ", contador7)
print("cantidad de multiplos de 9 encontrados en 1000 a 5000: ", contador9)