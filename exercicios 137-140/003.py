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
    Comprarm = input("Escreva o nome do comprador: ")
    PessoasRifa.append(Comprarm)
    if Comprarm == "":
        PessoasRifa.remove("")
        break

sorteio = choice(PessoasRifa)
print(f"o vencedor é {sorteio}")

