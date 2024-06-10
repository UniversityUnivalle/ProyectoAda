from itertools import combinations

puntos = [(1, 1), (1, 4), (4, 1), (4, 4)]

combinaciones = []
for r in range(3, len(puntos) + 1):
    combinaciones.extend(combinations(puntos, r))

for combinacion in combinaciones:
    print(combinacion)