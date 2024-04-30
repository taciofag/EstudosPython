# Enumerate

frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']


for indice, fruta in enumerate((frutas), 0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice, fruta)
