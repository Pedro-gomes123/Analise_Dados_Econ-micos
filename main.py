import duckdb as db
import coleta_dados as cd

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
        resposta_limpa = int(resposta_limpa)
   
        try:
            
            print(f"Você escolheu o número: {resposta_limpa}")


            match resposta_limpa:
                case 1:
                    try:
                        dias_str= input("Digite o número de dias para buscar os dados (padrão 365): ") 
                        num_dias = int(dias_str or 365)  # Usa 365 se a entrada for vazia
                        
                        
                    except ValueError:
                        print("Entrada inválida.")
                        num_dias = 365  # Valor padrão em caso de erro

                    print('Buscando os dados da Selic')

                    nome = 'selic'
                    codigo = indicadores[nome] 
                    tabela = cd.buscar_dados(codigo, nome, num_dias)
                       

                case 2:
                    print('Buscando os dados do Dólar')
                    nome = 'dolar'
                    codigo = indicadores[nome]
                    cd.Buscar_dados(codigo, nome)

                case 3:
                    print('Buscando os dados do IPCA')
                    nome = "ipca"
                    codigo = indicadores[nome]
                    cd.Buscar_dados(codigo, nome)
                case 4:
                    print('Encerrando o programa .......')
                    break
                case _:
                    print('Escolha invalida')
           
        except ValueError:
            print("Erro: Por favor, digite apenas um número.")

    







menu()