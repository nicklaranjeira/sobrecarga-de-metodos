class Gerador_Relatorio():
    def __init__(self, corpo_texto, titulo_corpo, titulo_corpo_rodape, varios_paragrafos, tudo_metadados ):
        self.__corpotexto =  corpo_texto
        self.__tituloCorpo = titulo_corpo
        self.__tituloCorpoRodape = titulo_corpo_rodape
        self.__variosParagrafos = varios_paragrafos
        self.__metadados =  tudo_metadados

    
    def Gerar(self, tipo, **kwargs):
            if tipo == 1:
                return self.__corpotexto                
            elif tipo == 2:
                return self.__tituloCorpo
            elif tipo == 3:
                return self.__tituloCorpoRodape
            elif tipo == 4:
                return self.__variosParagrafos
            elif tipo == 5:
                for chave, valor in kwargs.items():
                    print(f'{chave} - {valor}')
            else: 
                return print( "Opção inválida") 