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

        # Passo 1: Use o Pandas para criar uma tabela primeiro.
        df_pandas = pd.DataFrame(dados_json)

        # Passo 2: Entregue a tabela do Pandas para o DuckDB.
        tabela_duck = db.from_df(df_pandas)
        
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
    
print("--- INSPECIONANDO A BIBLIOTECA DUCKDB ---")
print(dir(db))
print("--- FIM DA INSPEÇÃO ---")