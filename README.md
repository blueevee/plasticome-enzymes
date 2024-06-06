[python-image]:https://img.shields.io/badge/python-^3.9-yellow
[flask-image]:https://img.shields.io/badge/flask-^2.3.2-gree
[poetry-image]: https://img.shields.io/badge/poetry-^1.5.1-blue


# 🍄 PLASTICOME ENZYMES 🍄
![1.0.0][python-image] ![1.0.0][poetry-image]
### Base de dados para armazenar informações referentes à ferramenta plasticome incluindo enzimas com atividade comprovada na degradação de plástico e seus metadados. Plasticome além dessa base de dados também é composta por uma API, [plasticome-backend](https://github.com/blueevee/plasticome-backend) que faz as análises recebidas pelo, [plasticome-frontend](https://github.com/blueevee/plasticome-frontend).


## 💙 Notas da desenvolvedora:
Essa é uma api para lidar com a base de dados nesse caso a escolhida foi PostgreSQL, e atualmente para acessar as rotas é necessário um token, para que esse token ser gerado é nessário autenticar na rota de autenticação com um usuário e senha, porém no momento atual desse commit o usuário e senha devem ser adicionados manualmente no banco de dados 😶😵. Adicionei também um [dump](./dump/) do banco de dados com as enzimas com degradação comprovada mapeadas até novembro de 2023.


## 😎 Quero mexer nesse projeto preciso de que?
1. Certifique-se de ter o python 3.9+
2. Tenha o gerenciador de pacotes do poetry instalado (pode usar outro e instalar as bibliotecas manualmente, mas recomendo fortemente o poetry)
3. Crie o ambiente virtual do poetry na raiz do projeto com `poetry shell`
4. Instale as dependências com `poetry install`
5. Tenha uma base de dados postgres disponível localmente ou em nuvem como (https://www.elephantsql.com/)
6. Duplique o arquivo [.env.example](/plasticome-metadata/.env.example)
7. Apaque o sufixo `.example` e preencha nesse arquivo todas as informações necessárias 
8. Descomente as linhas 33, 34 e 35 do arquivo [`metadata_enzyme_model.py`](/plasticome-metadata/plasticome_metadata/models/metadata_enzyme_model.py) e rode o arquivo para que as tabelas das enzimas sejam criadas
9. Descomente as linhas 16,17 e 18 do arquivo [`user_model.py`](/plasticome-metadata/plasticome_metadata/models/user_model.py) e rode o arquivo para que a tabela de usuários seja criada
10. Certifique-se que todas as tabelas foram devidamente criadas
11. Execute a função `create_user` do arquivo [`user_service.py`](/plasticome-metadata/plasticome_metadata/services/user_service.py), passando como parâmetros o usuário e a senha desejada, a função já fará o hash da senha antes de salvar no banco.
12. Com o usuário criado, você pode usar a rota de autenticação e conseguir o token que dará acesso à outras rotas como consulta às enzimas do banco, e até as análises do plasticome-backend



## 🔍 Comandos importantes para o desenvolvimento:
`task - l`: Comando do taskipy para listar as tarefas configuradas

`task lint`: Verifica se o código está seguindo as convenções da PEP8, usando blue e isort

`task docs`: Serve a documentação

`task teste`: Executa os testes da aplicação

`task run`: Executa o servidor flask


## 🧾 TO DO list para a eu do futuro:
- [ ] Adicionar testes unitários
- [ ] Melhorar segurança