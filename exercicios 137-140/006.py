"""
6. Crie um programa que leia um valor N, tal que N > 1. O programa deve gerar, aleatoriamente, uma lista L. Por fim, o programa deve calcular e imprimir a média geométrica dos N ele
mentos da lista..

"""

valorN = int(input('Escreva um valor maior que 1: '))

mult = 1
lista = [x for x in range(1, valorN+1)]

for t in lista:
    mult *= t

print(f'A média geométrica entre os valores {lista} = {(mult)*(1/len(lista))}')