from math import sqrt

"""
9. Construa um programa que solicite que o usuário informe 2 
números inteiros positivos. O programa deve calcular:
 a) O cubo do segundo número
 b) A média geométrica entre o primeiro e o segundo 
número, isto é, media_geometrica = sqrt(Num1*Num2)
"""

try:
    Num1 = int(input("Escreva um numero inteiro positivo: "))
    Num2 = int(input("Escreva um numero inteiro positivo: "))
    
    if ((Num1 and Num2) > 0 ):
        print(f"O cubo de {Num2} = {Num2**3} ")

        media_geometrica = sqrt(Num1*Num2)

        print(f"A media geometrica entre {Num1, Num2} = {media_geometrica}")
    else:
        print("Verifique se os numeros são inteiros positivos")

except ValueError:
    print(f"Erro: {ValueError}")
finally:
    print('O valor digitado deve estar errado')
