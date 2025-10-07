class GeradorRelatorio:
    def gerar(self, *args, titulo=None, rodape="Relatório gerado automaticamente", **kwargs):
    # *args guarda paragrafos
        relatorio = "" # vai adicionando tudo no relatório
        if titulo: # se título diferente de NONE
            relatorio += f"# {titulo}\n\n"

        for paragrafo in args:
            relatorio += f"{paragrafo}\n"

        if kwargs: # se existe printa
            relatorio += "\n---\n**Metadados:**\n"
            for chave, valor in kwargs.items():
                relatorio += f"- **{chave.capitalize()}:** {valor}\n"

        relatorio += f"\n---\n* {rodape} *" # printa o rodapé
        
        return relatorio