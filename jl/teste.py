from pdv_component import PdvComponent

crud = PdvComponent('bancotestepdv.db')

"""
campos = [{'nome_da_tabela':'cliente', 'nome_da_coluna':['id','nome', 'idade', 'data'], 'tipo':['integer', 'text', 'int', 'timestamp']},
            {'nome_da_tabela':'produto', 'nome_da_coluna':['id','nome', 'quantidade', 'valor', 'data'], 'tipo':['integer', 'text', 'int','int', 'timestamp']}]
crud.criar_tabela(campos)
"""
valores = [["poliana Mendes","caneca",2,"a vista", "cartao", "produçao", 0, 70, 24, 43, "2023-06-10"],
            ["ronygullity petriky","caneca",2 , "a prazo", "dinheiro", "produçao", 0, 700, 23, 4, "2023-06-10"],
            ["julia mendes","caneca",4 , "a prazo", "cartao", "entrega", 0, 90, 3, 2, "2023-06-10"],
            ["lorena mendes","chaveiro",1 , "a prazo", "cartao", "produçao", 0, 35, 23, 5, "2023-06-10"]]

#valores2 = [["caneca", 70, 35],["caneca polimero", 38, 30],["caneca jateada",49, 45],["caneca alça coraçao", 56, 60]]
#crud.inserir(tabela='cliente', valores=valores)
#crud.inserir(tabela='produto', valores=valores2)
crud.crud.inserir(tabela='vendas', valores=valores, data=True)



#resul = crud.read(tabela='vendas')
#print(resul)
#valores = [{'id':1, 'nome':'neide', 'idade':48}]
#crud.atualizar(tabela='cliente', valores=valores)
#resul = crud.read(tabela='cliente')
#print(resul)
#crud.deletar("cliente", 3)

