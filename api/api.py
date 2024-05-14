import requests
from pprint import pprint

# Get
# resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#Get com ID - Obter recurso único

resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2/')
pprint(resultado_get_id.json())

# # Post - Criar um novo recurso
# nova_tarefa = { 'completed': False,
#                 'title': 'CRIAR API',
#                 'userId': 1}


# resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos/', nova_tarefa)
# pprint(resultado_post.json())

# PUT - Alterar Recurso existente
# alterar_tarefa = {  'completed': True,
#                     'title': 'CRIAR API',
#                     'userId': 1}
# resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2',alterar_tarefa)
# pprint(resultado_put.json())

resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2').json()
pprint(resultado_delete)