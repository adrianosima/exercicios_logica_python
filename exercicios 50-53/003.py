import time

"""
3. Construa um programa que leia 2 números reais informados 
pelo usuário. Ao fim, o programa deve calcular e imprimir: 
    a. a soma dos dois valores
    b. o produto entre eles
"""

PrimeiroNumero = float(input("Escreva o primeiro número: "))
SegundoNumero = float(input("Escreva o segundo número: "))

print(f"A soma do primeiro número com o segundo = {PrimeiroNumero + SegundoNumero}")
print(f"A produto do primeiro número com o segundo = {PrimeiroNumero * SegundoNumero}")

time.sleep(3)
