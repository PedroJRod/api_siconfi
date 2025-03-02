# Projeto Siconfi API

O Sistema de Informações Contábeis e Fiscais do Setor Público Brasileiro - Siconfi é uma ferramenta criada com o objetivo de receber informações contábeis, financeiras e de estatísticas fiscais oriundas dos municípios, estados e da união. O Siconfi também compartilha esses dados através de sua API e é possível acessá-la através do R e do Python.

## Introdução

O site da API do Siconfi pode ser acessado no seguinte link: [Siconfi API Documentation](https://apidatalake.tesouro.gov.br/docs/siconfi/). Nele é possível obter os anexos relatórios, o RREO, o RGF e o DCA, além de outros dados de relatórios contábeis. Através do link, é possível construir um código para acessar a API de informações, entretanto, há pacotes e bibliotecas que oferecem funções prontas para importar os dados, e no qual as utilizaremos aqui.

## Estrutura do Repositório

Este repositório contém códigos em Python para acessar a API do Siconfi. Abaixo está a estrutura do repositório:

```
/c:/Users/Acer/Desktop/geop/
│
├── notebook.ipynb  # Jupyter Notebook com exemplos de acesso à API do Siconfi
└── README.md       # Este arquivo README
```

## Requisitos

- Python 3.6 ou superior
- Bibliotecas: `requests`, `pandas`, `json`

## Instalação

Para instalar as bibliotecas necessárias, você pode usar o pip:

```bash
pip install requests pandas
```

## Uso

### Acessando a API do Siconfi

O notebook `notebook.ipynb` contém exemplos de como acessar a API do Siconfi e manipular os dados retornados. Abaixo está um exemplo de como acessar os dados do RREO e do RGF.

#### Exemplo de Acesso ao RREO

```python
import requests, json
import pandas as pd

def RREO(an_exercicio, nr_periodo, co_tipo_demonstrativo, no_anexo, id_ente):
    url = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt//rreo?an_exercicio={an_exercicio}&nr_periodo={nr_periodo}&co_tipo_demonstrativo={co_tipo_demonstrativo}&no_anexo={no_anexo}&co_esfera=&id_ente={id_ente}'
    response = requests.get(url)
    dados = response.json()
    return dados

an_exercicio = "2024"
nr_periodo = "6"
co_tipo_demonstrativo = "RREO"
no_anexo = 'RREO-Anexo 13'
id_ente = "11"

dados = RREO(an_exercicio, nr_periodo, co_tipo_demonstrativo, no_anexo, id_ente)
dados = pd.DataFrame(dados['items'])
dados.head(3)
```

#### Exemplo de Acesso ao RGF

```python
def RGF(an_exercicio, in_periodicidade, nr_periodo, co_tipo_demonstrativo, co_poder, id_ente):
    url = f"https://apidatalake.tesouro.gov.br/ords/siconfi/tt//rgf?an_exercicio={an_exercicio}&in_periodicidade={in_periodicidade}&nr_periodo={nr_periodo}&co_tipo_demonstrativo={co_tipo_demonstrativo}&no_anexo=&co_esfera=&co_poder={co_poder}&id_ente={id_ente}"
    response = requests.get(url)
    dados = response.json()
    return dados

an_exercicio = "2024"
in_periodicidade = "Q"
nr_periodo = "3"
co_tipo_demonstrativo = "RGF"
id_ente = "11"
co_poder = "E"

dados = RGF(an_exercicio, in_periodicidade, nr_periodo, co_tipo_demonstrativo, co_poder, id_ente)
rgf_df = pd.DataFrame(dados['items'])
rgf_df.head(2)
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.