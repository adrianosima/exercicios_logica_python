"""

8. Crie um programa no qual o usuário informe o 
código do cargo de um funcionário (ver tabela 
abaixo) e o seu respectivo salário. Para encerrar 
a leitura dos dados, defina uma condição de parada 
(por exemplo, código do cargo igual a zero). 
Ao fim, o programa deve informar 
a média salarial dos nutricionistas.

CÓDIGO                  CARGO
 1                     Enfermeiro
 2                     Nutricionista
 3                     Médico

"""



from statistics import mean
from modulos import Menu

EnfermeiroSalario = []
NutricionistaSalario = []
MédicoSalario = []

parar = 1 

while parar != 0:
    Menu()
    Cargo = int(input("Escreva o cargo pretendido: "))
    
    if Cargo == 1:
        Salario = float(input("Escreva o salario: "))
        EnfermeiroSalario.append(Salario)
        parar = int(input("N para parar S para continuar"))
    
    elif Cargo == 2:
        Salario = float(input("Escreva o salario"))
        NutricionistaSalario.append(Salario)
        parar = int(input("0 para parar: "))

    elif Cargo == 3:
        Salario = float(input("Escreva o salario"))
        MédicoSalario.append(Salario)
        parar = int(input("0 para parar: "))

    else: print("Valor não encontrado")

print(mean(f"Media salarial dos Nutricionista {NutricionistaSalario}"))