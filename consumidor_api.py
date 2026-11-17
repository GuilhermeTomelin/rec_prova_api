import requests

def obter_dados_meteorologicos():
    # Consulta a API meteorológica local
    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

