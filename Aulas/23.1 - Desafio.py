# Crie 3 listas um com 5 frutas, uma com 5 cores, uma com 5 linguagens de programação
import os


frutas = ['maçã', 'banana', 'uva', 'pessego', 'melancia']
cores = ['azul', 'branco', 'amarelo', 'verde', 'vermelho']
linguagens_de_programacao = ['java', 'python', 'javascript', 'C#', 'C++']

# with open('frutas.txt', 'w', newline='', encoding='utf-8') as arquivo1:
#     for linha in frutas:
#         arquivo1.write(linha  + os.linesep)

# with open('cores.txt', 'w', newline='', encoding='utf-8') as arquivo2:
#     for linha in cores:
#         arquivo2.write(linha  + os.linesep)

with open('Top 5 Linguagens.txt', 'w', newline='', encoding='utf-8') as arquivo3:
    for linha in linguagens_de_programacao:
        arquivo3.write(linha  + os.linesep)

# with open('frutas.txt', 'a', newline='', encoding='utf-8') as arquivo1:
#     for linha in cores:
#         arquivo1.write(linha + os.linesep)
