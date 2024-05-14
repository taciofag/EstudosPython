import requests
import pprint

SIZE = 1
PAGE = 1

# URL da API que você deseja acessar
API_ENDPOINT = f'https://mutua.hagecard.com.br/api/public/pessoas/mutua/{SIZE}/{PAGE}'

# Sua chave de autenticação
API_KEY = "egfj1fky9l4dsfba3s1q6w4y8tk4lh9o"

# Cabeçalhos da solicitação com a chave de autenticação
headers = {
    #"Accept": "application/json",
    "x-api-key": API_KEY
}

# Realiza a solicitação GET para a API
response = requests.get(API_ENDPOINT, headers=headers)

# Verifica se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Extrai os dados da resposta
    dados = response.json()
    # Usa pprint para imprimir os dados de forma bonita
    pprint.pprint(dados)
else:
    # Se a solicitação falhar, imprime o código de status
    print(f"A solicitação falhou com o código de status {response.status_code}")