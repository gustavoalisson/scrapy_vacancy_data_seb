# Extração de Dados - Gupy :gear:

# :bulb: Objetivo
Extrair dados de (Cargo, Localidade, Efetividade) do site Gupy e inserir dados extraídos no Form. 

# 🚀 CHANGELOG
2024-01-16 - Versão: 1.0.0 
* Nessa primeira versão do projeto, o script é capaz de extrair os dados do Gupy de forma dinâmica e inserir todos os dados gerado do Dataframe no Forms.

# 🛠️ CONFIGURAÇÃO 
As configs estão em um arquivo .env de exemplo (sample.env), para o projeto rodar é necessário criar um arquivo .env de exemplo no raiz do projeto, conforme estabelecido no arquivo de exemplo. 

# 📁 EXECUTANDO LOCALMENTE
Para executar o projeto localmente em sua máquina é necessário seguir os seguintes passos:
* Clonar o projeto
* Criar uma virtualenv dentro do projeto
* Instalar as dependências necessárias que estão todas contidas em um arquivo (requirements.txt). No projeto foi criado dois arquivos requirements. (Txt e Lock) no Lock está todas as dependências do projeto.
  
`$ pip install -r requirements.txt`

* Verificar se o arquivo .env está configurado (Informações de como configurar no tópico de CONFIGURAÇÃO)
* Rodar o `python main.py`

**Observação 1:** O projeto está rodando em "background", caso deseje visualizar a execução do projeto de forma visual (em tela), será necessário comentar o argumento dentro de helpers/utilities.py

`options.add_argument('--headless')`

**Observação 2:** Na pasta logs do projeto é possível visualizar todo o log de fluxo do projeto.
Segue exemplo:
![image](https://github.com/gustavoalisson/scrapy_vacancy_data_seb/assets/52181576/382367a7-5713-47c2-80c0-5f42ba94e056)

# :pick: PRINCIPAIS TECNOLOGIAS USADAS
* Selenium - usado para Extração/Automação 
* Pandas - Manipulação de dados
* python-dotenv - Para guardar as configurações do projeto em um arquivo .env
* webdriver-manager - Faz a gestão automática do chromedriver



