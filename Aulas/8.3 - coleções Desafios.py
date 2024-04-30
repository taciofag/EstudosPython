# Desafio 1 = Ordene a lista abaixo pelo preço em ordem crescente
from operator import itemgetter

produtos = [
    {'nome': 'Celular',
     'preço': 1500},
    {'nome': 'Monitor',
     'preço': 500},
    {'nome': 'Microfone',
     'preço': 300},
]

produtos.sort(key=itemgetter('preço'))
print(produtos)

# Desafio 2 Ordene a lista abaixo por valor do equipamento em ordem decrescente
# Tuplas
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Desafio 3 = Ordene em ordem crescente a cotação moedas com base no valor da moeda
# matriz
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47],]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
