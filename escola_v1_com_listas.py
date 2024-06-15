"""Exibe relatório de crianças por atividade


Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Marciano"


sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica =  ["Erik", "Carlos", "Maria"]
aula_danca =  ["Gustavo", "Sofia", "Antonio"]


# Listar alunos em cada atividade por sala

atividades = [
    ("Ingles",aula_ingles),
    ("Musica",aula_musica),
    ("Dança",aula_danca),
]

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}")
    print("-" * 40)

     # sala1 que tem a interseção com a atividade

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

   

    # for aluno in atividade:
    #     if aluno in sala1:
    #         atividade_sala1.append(aluno)
    #     elif aluno in sala2:
    #         atividade_sala2.append(aluno)




    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print(f"-" * 40)
    print()
