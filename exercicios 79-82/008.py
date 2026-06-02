"""
 8.Considere uma equação do segundo grau, representada pela expressão
 ax**2 + bx + c = 0
Construa um programa no qual o usuário informe os valores das 
constantes a, b e c. Ao fim, o programa deve calcular e imprimir 
as raízes reais da equação. Caso não existam raízes reais, o pro
grama deve apresentar a mensagem “Não existem raízes reais.”
"""
from math import sqrt


a = float(input("Esccreva ovalor de a: ")) 
b = float(input("Esccreva ovalor de b: "))
c = float(input("Esccreva ovalor de c: "))

delta = ((b**2) - (4*a*c))

if delta < 0:
    print("Não existem raízes reais.")

elif delta >= 0:
    X1 = (-b + sqrt(delta))/(a*2)
    X2 = (-b - sqrt(delta))/(a*2)

    print(f"X1 = {X1} e X2 {X2}")
