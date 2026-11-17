## Monitoramento Meteorológico

Aplicação Python que consulta dados meteorológicos simulados
de Jaraguá do Sul - SC e apresenta os resultados no Streamlit.

# Arquivos
- consumidor_api.py: consulta a API.
- frontend.py: apresenta as informações.
- requirements.txt: dependências.
- .gitignore: arquivos ignorados pelo Git.

# Instalação:

- Ambiente virtual;
    python -m venv .venv

- Ativar no powershell:
    .\.venv\Script\Activate.ps1

# Preparação

A API utilizada está disponível em:
https://github.com/jpsvalentim/api-meteorologica-offline

A API deve estar funcionando em:
http://127.0.0.1:8000

Verificar a API:
http://127.0.0.1:8000/health

Testar pelo Postman:
GET http://127.0.0.1:8000/v1/forecast

# Parâmetros:
latitude = -26.4851
longitude = -49.0713