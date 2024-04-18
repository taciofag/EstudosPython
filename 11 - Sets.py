# SET

numeros = [2,2,5,8]
frutas = ['maça', 'uva', 'banana', 'maça', 'morango']

set_numeros = set(numeros)
set_frutas = set(frutas)

set_numeros.add(24)
print(set_numeros)

set_frutas.add('goiaba')
print(set_frutas)


numeros1 = [2,2,5,8]
numeros2 = [2,4,5,12]

a = set(numeros1)
b = set(numeros2)

print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))