from jl.pdv_crud import PdvCrud
import pandas as pd

class PdvComponent():
    def __init__(self, nome_banco) -> None:
        self.crud = PdvCrud(nome_banco=nome_banco)
        ver = self.crud.verificar()
        if ver != ['clientes','produtos','vendas']:
            self.iniciar()

    def iniciar(self):
        campos = [
            {'nome_da_tabela':'clientes', 
            'nome_da_coluna':['id','nome', 'numero', 'idade', 'sexo', 'endereço', 'numero_casa', 'cidade', 'data'], 
                                'tipo':['integer', 'text', 'integer', 'integer', 'text', 'text', 'text', 'text', 'timestamp']
                    },
            {'nome_da_tabela':'produtos', 
            'nome_da_coluna':['id','nome_produto', 'categoria', 'quantidade', 'valor', 'data'], 
                                'tipo':['integer', 'text','text', 'integer', 'integer', 'timestamp']
                    },
            {'nome_da_tabela':'vendas', 
            'nome_da_coluna':['id', 'nome_cliente', 'nome_produto', 'quantidade', 'forma_de_pagamento', 'tipo_pagamento', 'status_pedido', 'desconto', 'valor_total', 'cliente_id', 'produto_id', 'data'], 
                                'tipo':['integer', 'text', 'text', 'integer', 'text', 'text', 'text', 'integer', 'integer', 'integer', 'integer', 'timestamp']
                    }
                        ]
        self.crud.criar_tabela(campos=campos)

    def readtabelaVendas(self, condicao = None):
        """[["value1","value2","value3"]]"""
        cabecalho = [["Nome","Produto","Quantidade","Forma de pag/", "Tipo de pag/", "Valor R$","Data"]]
        values = self.crud.read(tabela="vendas", coluna="nome_cliente, nome_produto, quantidade, forma_de_pagamento, tipo_pagamento, valor_total, data", condiçao=condicao)
        
        for value in values:
            cabecalho.append(value)
        
        return cabecalho
    
    def inserirCsv(self, df):
        df = pd.read_csv(df)
        dflist = df.values.tolist()
        self.crud.inserir(tabela="vendas", valores=dflist, data=True)





