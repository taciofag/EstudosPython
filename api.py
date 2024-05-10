import requests
from pprint import pprint

# Get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

# Get com ID

resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_id.json())