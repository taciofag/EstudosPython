# Arrays

from array import array

# Tipos permitidos de array (Inteiros, decimais e caracteres)
# https://docs.python.org/pt-br/3.7/library/array.html
numeros = array('i',[2, 4, 8, 10, 20, 40])
print(numeros)
numeros.append(10) #inclui no final
print(numeros)
numeros.insert(5,200) #índice, valor
print(numeros)
numeros.pop(2) #Retira por índice (se não colocado o índice pega o último)
print(numeros)
numeros.remove(4) #remove pelo valor
print(numeros)
del numeros[2] # remover índice 2


print(numeros)