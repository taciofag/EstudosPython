import os

print(os.name)
print(os.listdir())
print(os.getcwd())
print(os.sep)
print(os.path.join(os.getcwd() + os.sep + 'senhas.txt'))
print(os.path.join(os.getcwd() + os.sep + 'Documentos' + os.sep + 'musica.mp3'))

caminho_senha = (os.path.join(os.getcwd() + os.sep + 'senhas.txt'))

print(os.path.dirname(caminho_senha)) #dirname = nome do diretório de um path
print(os.path.basename(caminho_senha)) #basename = nome do arquivo de um path
print(os.path.exists(os.getcwd() + os.sep + 'Aulas'))