# Arquivo JSON

import json
from pathlib import Path

# arquivo_carros_json = Path('carros.json').read_text()
# arquivo_json = json.loads(arquivo_carros_json)
# print(arquivo_json[0]['Marca'] +' '+ arquivo_json[0]['modelo'] +' R$ '+ str(arquivo_json[0]['Preço']))
# print(arquivo_json[1]['Marca'] +' '+ arquivo_json[1]['modelo'] +' R$ '+ str(arquivo_json[1]['Preço']))
# print(arquivo_json[2]['Marca'] +' '+ arquivo_json[2]['modelo'] +' R$ '+ str(arquivo_json[2]['Preço']))

items = Path('items.json').read_text(encoding='utf-8')
items_json = json.loads(items)

print(items_json[1]['name']['english'])