'''
Criar novo diretório dentro do diretório atual chamado Arquivos

Em um outro comando crie um novo diretório dentro do diretório 'Arquivos' chamado 'Arquivos Musicais'

Em apenas uma linha crie o diretório 'Musicas', como o sub-diretório 'Rock'

'''
import os
os.chdir('Aulas')




if os.path.exists('Arquivos'):
    print('diretório existente') # Criar novo diretório dentro do diretório atual chamado Arquivos
    print('Removendo pasta')
    os.rmdir('Arquivos')
    print('Pasta Removida')
    print('Criando pasta')
    os.mkdir('Arquivos')
    print('Pasta Criada')

else:
    print('Criando pasta')
    os.mkdir('Arquivos')
    print('Pasta Criada')
    
os.mkdir(os.path.join(os.getcwd() + os.sep + 'Arquivos' + os.sep +  'Arquivos Musicais')) # Em um outro comando crie um novo diretório dentro do diretório 'Arquivos' chamado 'Arquivos Musicais'

os.makedirs(os.path.join(os.getcwd() + os.sep + 'Arquivos' + os.sep +  'Arquivos Musicais' + os.sep +  'Musicas' + os.sep +  'Rock')) # Em apenas uma linha crie o diretório 'Musicas', como o sub-diretório 'Rock'