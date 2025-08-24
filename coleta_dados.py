import requests
import pandas as pd 
import datetime 
import requests as rq
import json as j




def Buscar_dados(codigo_serie, nome_serie , num_dias):
    data_atual = datetime.datetime.now() # pega no sistema a data do dia 
    data_duracao =datetime.timedelta(days=6) # pega no sistema o calendario do ano 
    data_inicio = data_atual - data_duracao


    data_atual_formatada =  data_atual.strftime('%d/%m/%Y')
    data_inicio_formatada = data_inicio.strftime('%d/%m/%Y')

    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicio_formatada}&dataFinal={data_atual_formatada }'

    response = rq.get(url)
    

    if response.status_code == 200:

        print('response funcionando')
        Dados_variaveis = response.json()
        df = pd.DataFrame(Dados_variaveis)
        print(df.head())
        
    else:

        print(f"response erro {response}")
    
