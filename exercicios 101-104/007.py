"""

7. Crie um programa no qual o usuário informe a idade de um 
número indeterminado de alunos. Para encerrar a leitura dos 
dados, o usuário deve informar uma idade negativa. No final, 
o programa deve mostrar a média aritmética entre a maior e a 
menor idade.

"""
import statistics 

IdadesAluno = []

while True:
    print("Digite uma idade negativa para prar!")
    Idades = int(input("Escreva a idade do aluno: "))
    if Idades > 0 :
        IdadesAluno.append(Idades)
    
    if Idades < 0:
        print(f"Maior Idade {max(IdadesAluno)}. Menor Idade {min(IdadesAluno)}. Media entre a maior e a menor idade {float((min(IdadesAluno) +max(IdadesAluno))/2)} ")
        break
