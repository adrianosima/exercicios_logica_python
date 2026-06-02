"""
 1. Construa um programa que receba um número inteiro positivo 
informado pelo usuário. Caso ele seja par, o programa deve calcular 
o seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu 
cubo. Ao fim, o programa deve imprimir o valor calculado. 
"""
try:

    NumeroInteiro = int(input("Escreva um numero inteiro: "))


    if (NumeroInteiro%2 == 0):
        print(f"o quadrado do  {NumeroInteiro} é igual a {NumeroInteiro**2}")

    elif (NumeroInteiro%2 != 0):
        print(f"o cubo do  {NumeroInteiro} é igual a {NumeroInteiro**3}")

    else:print("Valor desconhecido")
  
except ValueError:
    print("Valor incorreto")
