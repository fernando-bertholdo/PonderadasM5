# Resultados do teste automatizado

## Objetivo
Testar se o cadastro de um novo aluno funciona como esperado, mesmo sem ter uma API real funcionando. Foi usada uma resposta simulada (mock) para imitar a resposta que a API daria.

## Pré-condições
- Ter o Python instalado.
- Ter a biblioteca requests instalada.
- Ter os arquivos mockserver.py e teste_cadastrar_aluno.py na mesma pasta.
- Estar com o ambiente virtual ativado.

## Como foi feito o teste
1. A função mock_post_response() no arquivo mockserver.py simula a resposta da API, para que assim não haja necessidade de lug
2. No arquivo teste_cadastrar_aluno.py, o teste envia os dados de um novo aluno usando requests.post(), mas essa chamada é substituída pelo mock.
3. O teste verifica se a resposta tem o status 201 (Created) e se os dados do aluno retornam corretos.

## Resultado esperado
- A resposta deve ter status 201.
- A resposta deve conter os dados do aluno simulados no mock.

## Resultado que aconteceu
- O teste rodou sem erros.
- A mensagem “Teste de cadastro de aluno concluídoo (mock separado).” apareceu no terminal.
- Também apareceu a confirmação do Python que o teste passou:

![alt text](/Semana6/RESULTADOS_TESTE.png) 