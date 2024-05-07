import os

os.chdir(os.path.join(os.getcwd() + os.sep + 'Aulas'))

#criar pastas não existentes
#os.mkdir('22-teste')
#os.makedirs('22-teste' + os.sep + 'outroteste')

if os.path.isdir('21 - Aula21') == True:
    print('Esta pasta já existe')
else:
    os.mkdir('21 - Aula21')