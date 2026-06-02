"""

2. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). 
Para isso, devem ser informados 3 argumentos: 
    a) primeiro termo, 
    b) quantidade de termos e 
    c) razão.

"""

PrimeiroTermo = float(input("Escreva o primeiro: ")) 
QuantidadeTermo = int(input("Quantidade de termos: ")) 
razão = float(input("Escreva a rasão: "))

for i in range(1,QuantidadeTermo+1):
    Ntermo = (PrimeiroTermo + ((i-1)*razão))

    print(Ntermo)