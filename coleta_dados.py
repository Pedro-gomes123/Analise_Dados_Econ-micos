import requests
import duckdb as db
import datetime
import pandas as pd

def buscar_dados_bcb(codigo_serie, nome_serie, num_dias):
    
    data_fim = datetime.datetime.now()
    data_inicio = data_fim - datetime.timedelta(days=num_dias)
    
    data_inicio_formatada = data_inicio.strftime('%d/%m/%Y')
    data_fim_formatada = data_fim.strftime('%d/%m/%Y')

    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicio_formatada}&dataFinal={data_fim_formatada}'
    
    try:
        response = requests.get(url)
        print(f"DEBUG: URL Enviada -> {url}")
        response.raise_for_status()
        
        dados_json = response.json()
        if not dados_json:
            print(f"Atenção: A busca para {nome_serie} não retornou dados.")
            return pd.DataFrame()

        tabela_duck = db.from_objects(dados_json)
        
        consulta_sql = f"""
            SELECT
                strptime(data, '%d/%m/%Y') AS data,
                CAST(valor AS DOUBLE) AS "{nome_serie.lower()}"
            FROM tabela_duck
        """
        
        resultado_limpo = db.sql(consulta_sql)
      
        return resultado_limpo.to_df()

    except Exception as e: 
        print(f"Erro no processo para {nome_serie}: {e}")
        return pd.DataFrame() 