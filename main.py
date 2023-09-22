from jl import pdv_component
import pandas as pd

from telas.Janela_principal import JanelaPrincipal

class Pdv():
    def __init__(self,nome_banco) -> None:
        self.pc = pdv_component.PdvComponent(nome_banco=nome_banco)
        
        self.setup()


        
    def setup(self):
        vendas= self.pc.readtabelaVendas()

        self.janela = JanelaPrincipal(values=vendas, commandpesbotao=self.pesquisarPordata, comandoImprimirCsv=self.imprimirCsv)
        self.janela.mainloop()

    def pesquisarPordata(self):
        inicio, fim = self.janela.pegarData()
        query = f"Where data >= '{inicio}' and data <= '{fim}'"
        vendas= self.pc.readtabelaVendas(condicao=query)

        self.janela.values = vendas
        self.janela.fremeVendas()

    def imprimirCsv(self, csv_file):
        #csv_file = self.janela.abrir_arquivo()
        self.pc.inserirCsv(csv_file)
        #print(csv_file)




        
        
    #coisa para se fazer amanha
    #retornar o id na funçao inserir
    #ver como vai ficar a funçao set_clientes se vai ser uma lista ou nao de entrada 


if __name__ == "__main__":
    iniciar = Pdv('bancotestepdv.db')