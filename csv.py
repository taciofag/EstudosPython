# with open ('Listagem_Comparar.csv') as arquivo:
#     dados = arquivo.read()
#     print(dados)
from csv import DictReader

linha_atual = 1

with open('Listagem_Comparar.csv') as arquivo:
    dados = DictReader(arquivo, delimiter=';')
    for dado in dados:
        if linha_atual > 9 and linha_atual < 21:
            print (dado['ï»¿Titular'])
        
        linha_atual += 1