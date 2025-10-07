from classes import * 

relatorio = Gerador_Relatorio("corpo do texto", "Somente Título e Corpo", "Título, Corpo e rodapé", "Vários paragráfos",  tudo_metadados = {})
def EscolhaRelatório():
    escolha = input("Escolha o tipo de relatório que deseja imprimir\n1-Gerar somente texto\n2-Gerar corpo e texto\n3-Gerar um relatório com título, corpo de texto e um rodapé customizado\n4-Gerar um relatório que aceite múltiplos parágrafos para o corpo do texto.\n5-Gerar um relatório completo com metadados\n> ")
    if escolha == "1":
            print(relatorio.Gerar(tipo=1))
    elif escolha == "2":
            print(relatorio.Gerar(tipo=2))
        
    elif escolha == "3" :
            print(relatorio.Gerar(tipo=3))
        
    elif escolha == "4":
            print(relatorio.Gerar(tipo=4))
        
    elif escolha == "5":
            kwargs = {
                  "Autor" : "João",
                  "Data" : "12/09/2025",
                  "Versão" : '1'
           }
            print(relatorio.Gerar(tipo=5, **kwargs))
            
        
    else:
        print("Opção inválida")

    