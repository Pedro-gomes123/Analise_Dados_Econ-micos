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

            match resposta_limpa:
                case 1:
                    print('Buscando os dados da Selic')
                    nome = 'selic'
                    codigo = indicadores[nome] 
                    cd.buscar_dados(codigo, nome)

                case 2:
                    print('Buscando os dados do Dólar')
                    nome = 'Dólar'
                    codigo = indicadores[nome]
                    cd.Buscar_dados(codigo, nome)

                case 3:
                    print('Buscando os dados do IPCA')
                    nome = "ipca"
                    codigo - indicadores[nome]
                    cd.Buscar_dados(codigo, nome)
                case 4:
                    print('Encerrando o programa .......')
                    
                case _:
                    print('Escolha invalida')
           
        except ValueError:
            print("Erro: Por favor, digite apenas um número.")

    







menu()