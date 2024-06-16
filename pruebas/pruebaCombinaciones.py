from itertools import combinations

puntos = [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]


combinaciones = []
for r in range(3, len(puntos) + 1):
    combinaciones.extend(combinations(puntos, r))

for combinacion in combinaciones:
    print(combinacion)