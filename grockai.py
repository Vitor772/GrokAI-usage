import requests
import json

# Substitua pela sua chave de API
XAI_API_KEY = "xai-3IOFX7OXkQFny5wJMg0gQlR7KTxsySbWCErXZlcxAxY3kP9Cl2DaTZWEUV3cz5794cVqQJ5ECJ40j5LZ"

# Endpoint da API
url = "https://api.x.ai/v1/chat/completions"

# Dados da solicitação
payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": "Preciso de uma tela html e css estilo portfolio, bem bonita"
        }
    ],
    "model": "grok-beta",
    "stream": False,
    "temperature": 0
}

# Cabeçalhos
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {XAI_API_KEY}"
}

# Fazer a solicitação POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Verificar a resposta
if response.status_code == 200:
    print("Resposta da API:")
    print(response.json())
else:
    print(f"Erro: {response.status_code}")
    print(response.text)
