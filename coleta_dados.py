import requests
import duckdb as db
import datetime 
import requests as rq
import json as j




def Buscar_dados(codigo_serie, nome_serie , num_dias):
    data_atual = datetime.datetime.now() # pega no sistema a data do dia 
    data_duracao =datetime.timedelta(days=num_dias) # pega no sistema o calendario do ano 
    data_inicio = data_atual - data_duracao


    data_atual_formatada =  data_atual.strftime('%d/%m/%Y')
    data_inicio_formatada = data_inicio.strftime('%d/%m/%Y')

    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicio_formatada}&dataFinal={data_atual_formatada }'

    response = rq.get(url)
    

    if response.status_code == 200:

        print('response funcionando')
        Dados_variaveis = response.json()
        df = db.from_objects(Dados_variaveis)
        print(df.head())
        
    else:

        print(f"response erro {response}")
        return None

    consulta_sql = f"""
        SELECT 

        strptime(data, '%d/%m/%Y')  as data, 
        
        CAST(valor AS DOUBLE) as {nome_serie.lower()}
        
        FROM df
    """
    resultado_limpo = db.sql(consulta_sql)
    return resultado_limpo
    
