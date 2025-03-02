# siconfi_api.py
import requests
import pandas as pd

# Função para obter dados do RREO (Relatório Resumido de Execução Orçamentária)
def RREO(an_exercicio, nr_periodo, co_tipo_demonstrativo, no_anexo, id_ente):
    """
    Consulta os dados do RREO na API do Siconfi.
    :param an_exercicio: Ano do exercício
    :param nr_periodo: Período do relatório dentro do exercício
    :param co_tipo_demonstrativo: Tipo de demonstrativo (ex: 'RREO')
    :param no_anexo: Nome do anexo do relatório
    :param id_ente: Código IBGE do ente federativo
    :return: DataFrame com os dados do RREO
    """
    url = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio={an_exercicio}&nr_periodo={nr_periodo}&co_tipo_demonstrativo={co_tipo_demonstrativo}&no_anexo={no_anexo}&id_ente={id_ente}'
    response = requests.get(url)
    response.raise_for_status() #usado para verificar se a requisição HTTP foi bem-sucedida.
    return pd.DataFrame(response.json().get('items', []))

# Função para obter dados do RGF (Relatório de Gestão Fiscal)
def RGF(an_exercicio, in_periodicidade, nr_periodo, co_tipo_demonstrativo, co_poder, id_ente):
    """
    Consulta os dados do RGF na API do Siconfi.
    :param an_exercicio: Ano do exercício
    :param in_periodicidade: Periodicidade do relatório ('S' para semestral, 'Q' para quadrimestral)
    :param nr_periodo: Período do relatório dentro do exercício
    :param co_tipo_demonstrativo: Tipo de demonstrativo (ex: 'RGF')
    :param co_poder: Poder (E = Executivo, L = Legislativo, etc.)
    :param id_ente: Código IBGE do ente federativo
    :return: DataFrame com os dados do RGF
    """
    url = f'https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio={an_exercicio}&in_periodicidade={in_periodicidade}&nr_periodo={nr_periodo}&co_tipo_demonstrativo={co_tipo_demonstrativo}&co_poder={co_poder}&id_ente={id_ente}'
    response = requests.get(url)
    response.raise_for_status() #usado para verificar se a requisição HTTP foi bem-sucedida.
    return pd.DataFrame(response.json().get('items', []))

# main.py
if __name__ == "__main__":
    # Definição dos parâmetros para consulta do RREO
    an_exercicio = "2024"
    nr_periodo = "6"
    co_tipo_demonstrativo = "RREO"
    no_anexo = "RREO-Anexo 13"
    id_ente = "11"
    
    # Obtendo e exibindo os dados do RREO
    rreo_df = RREO(an_exercicio, nr_periodo, co_tipo_demonstrativo, no_anexo, id_ente)
    print("RREO Data:")
    print(rreo_df.head())
    
    # Definição dos parâmetros para consulta do RGF
    in_periodicidade = "Q"
    nr_periodo = "3"
    co_tipo_demonstrativo = "RGF"
    co_poder = "E"
    
    # Obtendo e exibindo os dados do RGF
    rgf_df = RGF(an_exercicio, in_periodicidade, nr_periodo, co_tipo_demonstrativo, co_poder, id_ente)
    print("\nRGF Data:")
    print(rgf_df.head())