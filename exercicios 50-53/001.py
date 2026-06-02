import time

"""
enunciado:

1. Um aluno iniciou seus estudos em geometria plana e, para 
validar se suas respostas estão corretos, solicitou sua ajuda. 
Sabendo que Area_triangulo = (base*altura)/2, construa um programa 
para auxiliar esse aluno.

"""

Base = float(input("Esceva o valor da base: "))
Altura = float(input("Escreva o valor da altura: "))

Area_triangulo = (Base*Altura)/2

print(f"A area do triangulo mede {Area_triangulo}")

time.sleep(2)
