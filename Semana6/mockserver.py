from unittest.mock import MagicMock

def mock_post_response():
    
    """
    mocka uma resposta da API para o cadastro de aluno no bd
    retorna um objeto mockado que simula um response do requests
    """

    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "id": 101,
        "nome": "Novo Aluno mockado",
        "data_nascimento": "2000-05-10",
        "unidade": "ETEC São Paulo"
    }
    return mock_response