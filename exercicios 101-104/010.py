"""

10. Uma turma da disciplina de Banco de Dados possui 
5 alunos. Construa um programa que leia duas notas 
e calcule a média aritmética de cada aluno. Ao fim, 
de acordo com a tabela abaixo, indique o percentual 
de alunos em Prova Final.

 FAIXA                     RESULTADO
 média < 2                 Reprovado
 2 ≤ média < 6             Prova Final
 média ≥ 6                 Aprovado

"""

alunosProvaFinal = []

for i in range(1,6):
    print(f"id do aluno em causa {i}")
    nota1 = float(input("Escreva as a primeira nota: "))
    nota2 = float(input("Escreva as a primeira nota: "))

    if i == 1:
        media = (nota1 + nota2)/2
        if 2 <= media < 6:
            alunosProvaFinal.append(1)
    
    elif i == 2:
        media = (nota1 + nota2)/2
        if 2 <= media < 6:
            alunosProvaFinal.append(1)

    elif i == 3:
        media = (nota1 + nota2)/2
        if 2 <= media < 6:
            alunosProvaFinal.append(1)

    elif i == 4:
        media = (nota1 + nota2)/2
        if 2 <= media < 6:
            alunosProvaFinal.append(1)

    elif i == 5:
        media = (nota1 + nota2)/2
        if 2 <= media < 6:
            alunosProvaFinal.append(1)

    percentual = int(len(alunosProvaFinal))/5

print(f"o percentual de alunos em exame final {percentual}, Numero de alunos no exame normal {len(alunosProvaFinal)}")