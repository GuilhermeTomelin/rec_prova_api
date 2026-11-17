import requests

resposta = requests.get(
    endereco,
    params=parametros,
    timeout=15
)
