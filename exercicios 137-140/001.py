"""

1. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). 
Para isso, devem ser informados 3 parâmetros de entrada: 
    a) primeiro termo da PA, 
    b) quantidade de termos da PA e 
    c) razão dessa PA. 
Construa um programa para carregar e 
imprimir uma lista contendo os termos 
da PA, bem como a soma dos elementos da PA.

"""

PrimeiroTermo = float(input("Escreva o primeiro: ")) 
QuantidadeTermo = int(input("Quantidade de termos: ")) 
razão = float(input("Escreva a rasão: "))

ListaTermo = []
soma = 0

for i in range(1, QuantidadeTermo+1):
    Ntermo = (PrimeiroTermo + ((i-1)*razão))
    ListaTermo.append(Ntermo)

for t in ListaTermo:
    soma += t

print(ListaTermo)
print(soma)
