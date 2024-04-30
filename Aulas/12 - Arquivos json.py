# Arquivo JSON

import json
from pathlib import Path

carros = [
    {'Marca': 'Kia','modelo': 'Cerato','Preço': 32000},
    {'Marca': 'Hyunday','modelo': 'Elantra','Preço': 85000},
    {'Marca': 'Fiat','modelo': 'Uno','Preço': 7500}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

arquivo_carros_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carros_json)
print(arquivo_json[0]['Marca'] +' '+ arquivo_json[0]['modelo'] +' R$ '+ str(arquivo_json[0]['Preço']))
print(arquivo_json[1]['Marca'] +' '+ arquivo_json[1]['modelo'] +' R$ '+ str(arquivo_json[1]['Preço']))
print(arquivo_json[2]['Marca'] +' '+ arquivo_json[2]['modelo'] +' R$ '+ str(arquivo_json[2]['Preço']))