import requests
from tests.config import BASE_URL

def get_tarefas():
    # Faz uma requisição para a url de listar tarefas
    response = requests.get(f"{BASE_URL}/tarefas")

    # Verifica o status code da resposta
    assert response.status_code == 200

    # Converte a resposta pra json
    data = response.json()

    # Verifica se a resposta não está vazia
    assert len(data) > 0
    assert "tarefas" in data[0]

