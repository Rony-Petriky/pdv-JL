import sqlite3
import subprocess
from datetime import datetime
#criando banco
class Crud():
    def __init__(self, nome_banco:str) -> None:
        self.banco = sqlite3.connect(nome_banco)
        #criando cursor
        self.cursor = self.banco.cursor()

    
    def criar_tabela(self, campos):
        
        for campo in campos:
            nome_da_tabela = campo['nome_da_tabela'] 
            nome_da_coluna = campo['nome_da_coluna']
            tipo = campo['tipo']
            nomecolun = ""
            flag = 0
            for nome in nome_da_coluna:
                nomecolun += f"{nome} {tipo[nome_da_coluna.index(nome)]}"
                flag += 1
                if flag <= (len(tipo) - 1):
                    nomecolun += ","
                

            CREATE_TABLE = f"CREATE TABLE {nome_da_tabela} ({nomecolun})"
            self.cursor.execute(CREATE_TABLE)
           
            dados  = self.cursor.execute("SELECT name FROM sqlite_master")
            dados = dados.fetchone()
            print("Tabela", nome_da_tabela, "criada")
        dados  = self.cursor.execute("SELECT name FROM sqlite_master")
        dados = dados.fetchone()

        #comando = "sqlite3 bancoteste.db '.tables'"
        #shel = subprocess.check_output(comando, shell=True)
        #tabelas = shel.split()
    

    def read(self, tabela, coluna='*', condiçao=None):
        query = f"SELECT {coluna} FROM {tabela} {condiçao}"
        ds = self.cursor.execute(query)
        ds = ds.fetchall()
        dados = []
        for d in ds:
            dado = list(d)
            dados.append(dado)

        return dados

    def inserir(self,tabela, valores):
        ids = self.read(tabela=tabela, coluna='id', condiçao='ORDER BY id') 
        id = 0
        if len(ids) > 0:
            quan_ids = len(ids)
            quan_ids = int(quan_ids) - 1
            id = ids[quan_ids]
            id = id[0]

        
        for valor in valores:
            condiçao = ''
            id = id + 1
            for v in valor:
                classe = str(type(v))
                if classe == "<class 'str'>":
                    condiçao += f",'{v}' "
                else:
                    condiçao += f",{v} "
            date = datetime.now()
            print(date.date())
            query = f"INSERT INTO  {tabela} VALUES({id} {condiçao} ,{str(date.date())})"
            self.cursor.execute(query)
            self.banco.commit()
        print(id, " linhas adicionadas")

    def deletar(self,tabela, id):
        query = f'DELETE FROM {tabela} WHERE id = {id}'
        print(query)
        self.cursor.execute(query)
        self.banco.commit()
        print("apagado")

    def translist(dic, dici):
        valorlist = []
        for valor in dici:
            valorlist.append(valor)
        return valorlist
        
    def atualizar(self, tabela, valores):
        for valor in valores:
            id = valor['id']
            chaves = valor.keys()
            chaves = self.translist(valor.keys())
            valores = valor.values()
            valores = self.translist(valores)
            condiçao = ""
            flag = 0
            for chave in chaves:
                condiçao += f"{chave} = "
                elemnto = str(type(valores[chaves.index(chave)]))
                if elemnto == "<class 'str'>":
                    condiçao += f"'{valores[chaves.index(chave)]}' "
                else:
                    condiçao += f"{valores[chaves.index(chave)]} "

                flag += 1
                if flag <= (len(valores) - 1):
                    condiçao += ", "


            query = f"UPDATE {tabela} SET {condiçao} WHERE id= {id}"
            self.cursor.execute(query)
            self.banco.commit()
            print('atualizado')
    
        








#banco = sqlite3.connect('crv.db')
#cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#dados = cursor.execute("SELECT name FROM sqlite_master")
#print(dados.fetchone())
#criando cursor
"""cursor = banco.cursor()

#criar tabela
cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#inserindo elementos na tabela
cursor.execute("INSERT INTO movie VALUES()")
cursor.commit()

#read
cursor.execute("SELECT * FROM pessoas")"""