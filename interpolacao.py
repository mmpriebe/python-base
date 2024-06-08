email_tmpl = """
olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver
%(texto)s

Clique agora em %(quantidade)d disponiveis!

Preco promocional %(preco).2f
"""


 for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "Caneta",
    "texto": "Escreve muito bem", "link": "www.canetalegal.com.br",
    "quantidade": 1, "preco": 50.5,})


