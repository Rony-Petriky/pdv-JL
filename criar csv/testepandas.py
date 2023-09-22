import pandas as pd

import random

x = random.randint(0,3)




venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
        }
nome_cliente = ['POliana Mendes', 'Ronygullity Petriky', 'Lorena Mnedes', 'Julia mendes']
nome_produto = ['caneca branca', 'chvaveiro', 'caneca polimero', 'camiseta poliester',]
quantidade = [1,2,3,4]
forma_de_pagamento = ['a vista', 'a prazo', 'a vista', 'a prazo'  ]
tipo_pagamento = ['dinheiro', 'cartao', 'dinheiro', 'cartao']
status_pedido = ['agendamento pag/', 'personaliaçao', 'preparaçaop de arte', 'pedido pronto']
desconto = [0, 1, 2, 3]
valor_total = [70, 35, 45, 15]
cliente_id = [1, 2, 3, 4]
produto_id = [5, 6, 7, 8]
data = ['2023-06-16','2023-07-16','2023-08-16','2023-09-16']

nome_cliente1 = []
nome_produto1 = []
quantidade1 = []
forma_de_pagamento1 = []
tipo_pagamento1 = []
status_pedido1 = []
desconto1 = []
valor_total1 = []
cliente_id1 = []
produto_id1 = []
data1 = []

i = 0
while i < 30 :
    x = random.randint(0,3)

    nome_cliente1.append(nome_cliente[x])
    nome_produto1.append(nome_produto[x])
    quantidade1.append(quantidade[x])
    forma_de_pagamento1.append(forma_de_pagamento[x])
    tipo_pagamento1.append(tipo_pagamento[x])
    status_pedido1.append(status_pedido[x])
    desconto1.append(desconto[x])
    valor_total1.append(valor_total[x])
    cliente_id1.append(cliente_id[x])
    produto_id1.append(produto_id[x])
    data1.append(data[x])
    
    i = i+1
    #print(i)

vendas = {
    'nome_cliente':nome_cliente1,
     'nome_produto':nome_produto1,
      'quantidade':quantidade1,
       'forma_de_pagamento':forma_de_pagamento1,
        'tipo_pagamento':tipo_pagamento1,
         'status_pedido':status_pedido1,
          'desconto':desconto1,
           'valor_total':valor_total1,
            'cliente_id':cliente_id1,
             'produto_id':produto_id1,
              'data':data1
}

df = pd.DataFrame(vendas)
df.to_csv("vendas_csv4.csv", encoding = 'utf-8', index = False)

print("csv gerado com sucesso")

