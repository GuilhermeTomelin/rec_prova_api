import requests # Biblioteca

def obter_dados_meteorologicos():
    # Consulta a API meteorológica local:
    url = "http://127.0.0.1:8000/v1/forecast"
    # Parâmetros de consulta:
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    try:
        resposta = requests.get(url, params=parametros, timeout=10) # A resposta vai receber o parâmentro definido e a url para a consulta.
        resposta.raise_for_status()

        # Obtém os dados atuais do JSON
        atual = resposta.json()["current"]
        # Informações que ele vai retornar:
        return {
            "temperatura": atual["temperature_2m"],
            "umidade": atual["relative_humidity_2m"],
            "sensacao": atual["apparent_temperature"],
            "precipitacao": atual["precipitation"],
            "vento": atual["wind_speed_10m"],
            "horario": atual["time"]
        }
        # Except utilizado para os tipos de erros que podem ser retornados:
    except (requests.RequestException, ValueError, KeyError, TypeError) as erro:
        raise RuntimeError(f"Erro ao consultar a API: {erro}") from erro #Mensagem de erro mostrada ao usuario