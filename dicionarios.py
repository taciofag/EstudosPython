# Dicionários

'''
Pessoa
    Nome
    Idade
    Altura

'''

pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]

dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}

pessoa2 = dict(nome='Carol', idade='18', altura=1.60)


print(pessoa2.items())

for item in dicionario_pessoa.items():
    print(item)
    print(item[1])
