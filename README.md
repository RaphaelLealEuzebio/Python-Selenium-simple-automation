##🚀 FastAPI + Selenium Automation DemoEste projeto é uma API desenvolvida em FastAPI integrada ao Selenium, focada na automação de processos e integração entre sistemas. A aplicação recebe um termo via requisição HTTP e orquestra uma automação real no navegador.


##🧠 Objetivo do ProjetoDemonstrar proficiência em Python para back-end.Criação de APIs REST performáticas.Integração de fluxos de automação web (Web Scraping/Automation).Aplicação de Clean Code e organização modular.

##🛠️ Tecnologias UtilizadasTecnologiaDescriçãoPython 3.10+Linguagem base do projeto.FastAPIFramework web moderno e rápido.SeleniumFerramenta para automação de navegadores.PydanticValidação de dados e gerenciamento de schemas.UvicornServidor ASGI de alta performance.Chrome/DriverNavegador e driver para execução da automação.


##📂 Estrutura do ProjetoPlaintext.
├── main.py           # Definição dos Endpoints e inicialização da API
├── automation.py     # Core da lógica de automação (Selenium)
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação

##▶️ Como Executar o Projeto

#1. Clone o repositório:Bash 

git clone https://github.com/seu-usuario/fastapi-selenium-demo.git
cd fastapi-selenium-demo

#2. Configure o ambiente virtual:Bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

#3. Instale as dependências:Bash
pip install -r requirements.txt

#4. Inicie o servidor:Bash

uvicorn main:app --reload

A API estará disponível em: http://127.0.0.1:8000📡 Endpoints Disponíveis1. Health CheckGET /Descrição: Verifica se a API está online.Resposta: {"API": "Funcionando Corretamente"}

#2. Informações do ProjetoGET /infoDescrição: 

Retorna metadados da aplicação.

#3. Executar Automação

POST /searchBody (JSON):JSON{
  "term": "FastAPI Selenium"
}
Resposta:JSON{
  "received_term": "FastAPI Selenium",
  "result": "FastAPI Selenium - Pesquisa Google"
}

#⚠️ Observações Importantes[!IMPORTANT]Sincronia: O Selenium é executado de forma síncrona para fins de demonstração. Em cenários de alta demanda, recomenda-se o uso de BackgroundTasks do FastAPI ou sistemas de mensageria como Celery.

##👨‍💻 AutorRaphael Leal Euzebio Python Developer | Back-end | AutomaçãoLinkedInGitHub