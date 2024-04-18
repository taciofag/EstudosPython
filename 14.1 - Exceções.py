try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[15]-1)
except IndexError as erro_de_index:
    print('tá errado')
    print(erro_de_index)
except NameError as erro_de_nome:
    print('tá errado tbm')