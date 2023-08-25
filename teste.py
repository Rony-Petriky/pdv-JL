from Crud import Crud

crud = Crud('bancoteste.db')


campos = [{'nome_da_tabela':'cliente', 'nome_da_coluna':['id','nome', 'idade', 'data'], 'tipo':['integer', 'text', 'int', 'timestamp']}]
crud.criar_tabela(campos)

valores = [["poliana", 24],["rony", 27],["julia",10],["lorena", 3]]
crud.inserir(tabela='cliente', valores=valores)


"""
resul = crud.read(tabela='cliente')
print(resul)
valores = [{'id':1, 'nome':'neide', 'idade':48}]
crud.atualizar(tabela='cliente', valores=valores)
resul = crud.read(tabela='cliente')
print(resul)
#crud.deletar("cliente", 3)

"""