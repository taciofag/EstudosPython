# Ordenar por propriedades

from operator import itemgetter
products = [
    ('Cellphone', 7500),
    ('Macbook Pro', 9000),
    ('Mic', 550),
    ('Mic', 549),
]

products.sort(key=itemgetter(1))
print(products)
