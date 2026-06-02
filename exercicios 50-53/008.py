"""
8. Construa um programa que receba do usuário o valor do 
salário mínimo atual. Na sequência, o programa deve solicitar 
que o usuário informe o valor do seu salário mensal. Ao fim, o 
programa deve calcular a quantidade de salários mínimos recebidos 
pelo usuário. 

"""

SalarioMinimoAtual = float(input("Informe o Salario Minimo Atual: "))
SalarioMensalAtual = float(input("Informe o Salario Mensal Atual: "))

QuantidadeSalarioMinimo = SalarioMensalAtual/SalarioMinimoAtual

print(f"Tu recebes {QuantidadeSalarioMinimo} Salarios minimos")
