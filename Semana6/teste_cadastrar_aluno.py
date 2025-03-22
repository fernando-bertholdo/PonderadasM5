import unittest
from unittest.mock import patch
import requests
from mock_server import mock_post_response  # Importando o mock

class TestCadastroAluno(unittest.TestCase):
    @patch('requests.post', return_value=mock_post_response())
    def test_cadastrar_aluno(self, mock_post):
        
        """
        Caso de teste: cadastrar aluno novo
        Objetivo é simular a requisição de cadastro e validar a resposta esperada.
        
        """

        # dados de um aluno para teste
        novo_aluno = {
            "nome": "Novo Aluno Mockado",
            "data_nascimento": "2000-05-10",
            "unidade": "ETEC São Paulo"
        }

        # simulando uma requisição (mockada)
        url = "http://mock-api/aluno"
        response = requests.post(url, json=novo_aluno)

        # Verificações
        self.assertEqual(response.status_code, 201, "Deveria retornar 201 Created")
        self.assertEqual(response.json(), mock_post_response().json.return_value, "JSON retornado não confere")

        print("Teste de cadastro de aluno concluídoo (mock separado).")

if __name__ == "__main__":
    unittest.main()