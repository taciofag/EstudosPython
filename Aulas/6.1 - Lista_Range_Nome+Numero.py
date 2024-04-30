# Enumerate

lista_de_nomes = []

nomes = 'nome'
for nome in range(1, 11):
    nomes_enumerados = (f'{nomes}{nome}')
    lista_de_nomes.append(nomes_enumerados)
    if nome == 5:
        lista_de_nomes.append('metade')
        
print(lista_de_nomes)



