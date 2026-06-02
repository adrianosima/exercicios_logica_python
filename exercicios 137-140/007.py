"""
7. Crie um programa que gere, aleatoriamente, uma matriz M, com elementos no intervalo [0, 1]. A quantidade de linhas e de colunas de M devem ser informadas pelo usuário. Ao fim, o programa deve informar se M é uma matriz nula.

"""
from random import randrange

lin = int(input('Numero de linha: '))
col = int(input('Numero de linha: '))

soma = 0
cont = 0

M = [[randrange(0, 2) for i in range(col)] for i in range(lin)]

for i in M:
  for t in i:
    if t == 0:
      cont += 1
      
    soma +=1

if cont == soma:
  print(f'Matrix nula {M}')    