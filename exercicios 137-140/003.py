"""

3. Uma turma de formandos está vendendo 
rifas para angariar recursos financeiros 
para sua cerimônia de formatura. Construa 
um programa para cadastrar os nomes das 
pessoas que compraram a rifa. Ao fim, 
o programa deve sortear o ganhador do 
prêmio e imprimir o seu nome.

"""
from random import choice

PessoasRifa = []

while True:
    Compraram = input("Escreva o nome do comprador: ")
    
    if Compraram == "":
        break
    else:
        PessoasRifa.append(Compraram)


sorteio = choice(PessoasRifa)
print(f"o vencedor é {sorteio}")

