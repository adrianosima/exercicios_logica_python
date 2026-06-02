"""
6. Considere uma equação do segundo grau, representada 
pela expressão ax^2 + bx + c = 0
Construa um programa no qual o usuário informe os valores 
das constantes a, b e c. Ao fim, o programa deve calcular 
e imprimir o valor de delta. Sabe-se que ∆ =b2-4ac.
"""
a = float(input("Esccreva ovalor de a: ")) 
b = float(input("Esccreva ovalor de b: "))
c = float(input("Esccreva ovalor de c: "))

delta = ((b**2) - (4*a*c))

print(f"∆ = {delta}")
