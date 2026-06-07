🚀 FastAPI do Zero

Projeto desenvolvido durante o curso FastAPI do Zero, ministrado por Eduardo Mendes (Dunossauro).

O objetivo deste repositório é documentar minha jornada de aprendizado em desenvolvimento de APIs modernas com Python, aplicando boas práticas, testes automatizados e ferramentas utilizadas no mercado.

📚 Sobre o curso

O FastAPI do Zero é um curso gratuito e aberto que ensina a construir uma API completa com Python utilizando o framework FastAPI, desde a configuração do ambiente até o deploy em produção.

Durante o curso, são abordados conceitos como:

Desenvolvimento de APIs REST com FastAPI;
Validação de dados com Pydantic;
Testes automatizados com Pytest e Coverage;
Formatação e análise estática de código com Ruff;
Gerenciamento de dependências com Poetry;
Migrations com Alembic;
Banco de dados com SQLAlchemy;
Autenticação e autorização com JWT;
Programação assíncrona;
Docker e PostgreSQL;
Integração contínua com GitHub Actions;
Deploy da aplicação.
🛠 Tecnologias utilizadas
Python 3.14
FastAPI
Uvicorn
Pydantic
SQLAlchemy
Alembic
Pytest
Coverage
Ruff
Poetry
Taskipy
Docker
PostgreSQL
Git e GitHub

📂 Estrutura do projeto
.
├── fastapi_zero/
├── tests/
├── pyproject.toml
├── poetry.lock
├── README.md
└── .gitignore
▶️ Executando o projeto

Clone o repositório:

git clone <url-do-repositorio>

Entre na pasta:

cd fastapi_zero

Instale as dependências:

poetry install

Ative o ambiente virtual:

poetry shell

Execute a aplicação:

task run

A API ficará disponível em:

http://localhost:8000

Documentação automática:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🧪 Executando os testes
task test

Gerando relatório de cobertura:

task post_test
📖 Material de estudo
Curso FastAPI do Zero: https://fastapidozero.dunossauro.com/estavel/
Repositório do curso: https://github.com/dunossauro/fastapi-do-zero
👨‍🏫 Créditos

Curso criado por Eduardo Mendes (@dunossauro), referência na comunidade Python brasileira.

📌 Objetivo deste repositório

Este projeto tem caráter educacional e foi criado para registrar meus estudos e evolução no desenvolvimento de APIs com FastAPI.