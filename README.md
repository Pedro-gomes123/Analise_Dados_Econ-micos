# 📊 Dashboard de Indicadores Econômicos

Este projeto é um dashboard web dinâmico e interativo, construído em Python com Flask e DuckDB, que permite a visualização de dados de importantes indicadores econômicos do Brasil.

## 🚀 Funcionalidades

* Interface web interativa com HTML, CSS e JavaScript.
* Seleção de múltiplos indicadores: SELIC, Dólar e IPCA.
* Período de busca flexível definido pelo usuário.
* Geração de gráficos dinâmicos utilizando a biblioteca Chart.js.
* Backend robusto com Flask para servir os dados via API.
* Processamento e limpeza de dados em tempo real com DuckDB e SQL.


## 🛠️ Tecnologias Utilizadas

* **Backend:** Python
* **Servidor Web:** Flask
* **Processamento de Dados:** DuckDB, SQL
* **Frontend:** HTML5, CSS3, JavaScript
* **Visualização de Dados:** Chart.js
* **API:** Consumo da API de Séries Temporais do Banco Central do Brasil (SGS)

## ⚙️ Como Executar o Projeto

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.10](https://www.python.org/) ou superior
* [pip](https://pip.pypa.io/en/stable/installation/)

### Instalação
1.  Clone o repositório:
    ```bash
    git clone do repositorio 
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd seu-repositorio
    ```
3.  (Opcional, mas recomendado) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4.  Ative o ambiente virtual:
    * No Windows: `.\venv\Scripts\activate`
    * No Linux/Mac: `source venv/bin/activate`

5.  Instale as dependências a partir do arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Execução
1.  Para iniciar o servidor Flask, rode o comando:
    ```bash
    python app.py
    ```
2.  Abra seu navegador e acesse `http://127.0.0.1:5000`.

## 👨‍💻 Autor

**Pedro Gomes**

* LinkedIn: ``
* GitHub: `@Pedro-gomes123`