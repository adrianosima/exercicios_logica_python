from math import sqrt

"""
Construa um programa que tem como dados de entrada 
dois pontos quaisquer no plano cartesiano: P1 e P2. Considere 
que P1 é definido pelas coordenadas  x1 e y1, enquanto P2 por  
x2 e y2. O programa deve calcular e escrever a distância entre 
os pontos P1 e P2. A fórmula que calcula a distância entre os 
dois pontos é dada por: d = sqrt((x2-x1)^2 +(y2-y1)^2) 
Para receber os dados de entrada, use as variáveis x1, y1, 
x2 e y2.
 Dica: A função que calcula a raiz quadrada de um número real 
é a sqrt (square root). Para usá-la, importe-a da biblioteca math 
da seguinte forma: from math import sqrt. 
"""

x1 = float(input("Escreva o valor para x1: "))
y1 = float(input("Escreva o valor para y1: "))
x2 = float(input("Escreva o valor para x2: "))
y2 = float(input("Escreva o valor para y2: "))

d = sqrt((((x2-x1)**2) + ((y2-y1)**2)))

print(f"A distancia entre os pontos {x1, y1, x2, y2} é igual á {d}")
