# Tuplas
# não fazer isso
site1 = 'youtube.com.br'
site2 = 'facebook.com'
site3 = 'instagram.com'
# ou
valor1 = 23
valor2 = 18
valor3 = 65


# Criação de Tupla
sites = ('youtube.com.br', 'facebook.com', 'instagram.com',54,True,False)
valores = (23, 18, 65)

print(f'{sites[1]}, \n{valores[2]}')

# sites[1] = 'google' - Não pode permitir novos valores a tuplas

dados_do_sistema = sites+valores

print(dados_do_sistema)
print(dados_do_sistema[4])