# Ordenar por propriedades

from operator import itemgetter
nomes = ['Zack', 'Camilla', 'Julius', 'Vincent']
values = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]

pessoas = [
    {'nome': 'John',
     'idade': 32,
     'nivel_acesso': 2},
    {'nome': 'Carol',
     'idade': 18,
     'nivel_acesso': 3},
    {'nome': 'Thomas',
     'idade': 45,
     'nivel_acesso': 5},
    {'nome': 'Tacio',
     'idade': 31,
     'nivel_acesso': 1}
]


pessoas.sort(key=itemgetter('nome'))
print(pessoas)
