import pandas as pd 
import coleta_dados as cd 

codigo_serie = ['selic','dolar','ipca' ]

nome_serie = [432, 1, 433]

indicadores = {
    'selic': 432,
    'dolar': 1,
    'ipca': 433
    }


def menu(): 
    while True:
        print("\n--- Dashboard Econômico ---") 
        print("Escolha uma opção para visualizar o gráfico:")
        print("[1] Taxa SELIC")
        print("[2] Cotação do Dólar")
        print("[3] Inflação (IPCA)")
        print("[4] Sair do programa")
        
        resposta_str = input("Digite o número da sua escolha: ")

  
        resposta_limpa = resposta_str.strip() 
        
   
        try:
            resposta_int = int(resposta_limpa)
            print(f"Você escolheu o número: {resposta_int}")
           
        except ValueError:
            print("Erro: Por favor, digite apenas um número.")


menu()