# Como criar listas
# Criar listas usando loop
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Tacio', 'Chris', 'Johnny']


def aprovar_pessoa(nome):
    return nome + ' Aprovado'


print(list(map(aprovar_pessoa, nomes)))
