"""

6. Construa um programa que receba uma lista contendo a estatura dos alunos de uma escola. Crie um relatório que informe a
    a. menor estatura 
    b. maior estatura 
    c. média das estaturas informadas

"""
import statistics


EstaturAluno = []

NumeroStatura = int(input('quantas estaturas pretendes incluir: '))


for i in range(1, NumeroStatura+1):
    Estaturas = float(input("Escreva a estatura: "))
    EstaturAluno.append(Estaturas)


print(f"A Maior estatura é {max(EstaturAluno)}\nA Menor estatura é {min(EstaturAluno)}\n A Media entre as estaturas é {statistics.mean(EstaturAluno)}")