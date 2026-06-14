"""

Crie um programa que apresente o seguinte menu
 Cálculo das áreas de figuras
 geométricas:

 1. Círculo
 2. Triângulo
 3. Retângulo

 Qual figura deseja calcular a 
 área? ____

"""
from modulo import Menu, triangulo, retangulo, circulo

Menu()
opção = input('Qual figura pretendes calcular: ')

if opção == '1':
    raio = float(input('Informe o   valor do raio: '))
    print(circulo(raio))

elif opção =='2':
    base = float(input('Informe o valor da base: '))
    haltura = float(input('Informe o valor da haltura: '))

    print(triangulo(base, haltura))

elif opção == '3':
    base = float(input('Informe o valor da base: '))
    haltura = float(input('Informe o valor da haltura: '))
    print(retangulo())

else:
    print('Opção invalida [1-3]')