# Ordenar por propriedades

from operator import itemgetter

matriz = [[5, 74], [1, 21], [100, 12], [6, 100]]

matriz.sort(key=itemgetter(1))
print(matriz)
