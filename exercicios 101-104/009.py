"""
9. Com base na tabela salarial da 
questão anterior, crie um programa 
que informe a quantidade de médicos 
com salários superiores a R$ 4.500,00. 

"""

def Menu():
    print("""

      CÓDIGO                  CARGO
        1                     Enfermeiro
        2                     Nutricionista
        3                     Médico


    """)

from statistics import mean

EnfermeiroSalario = []
NutricionistaSalario = []
MédicoSalario = []

parar = 1 
Numerosmedicos = 0

while parar != 0:
    Menu()
    Cargo = int(input("Escreva o cargo pretendido: "))
    
    if Cargo == 1:
        Salario = float(input("Escreva o salario: "))
        EnfermeiroSalario.append(Salario)
    
    elif Cargo == 2:
        Salario = float(input("Escreva o salario"))
        NutricionistaSalario.append(Salario)

    elif Cargo == 3:
        Salario = float(input("Escreva o salario"))
        MédicoSalario.append(Salario)

    else: print("Valor não encontrado")


for i in MédicoSalario:
    print(MédicoSalario)
    if i > 4500:
        Numerosmedicos +=1

    print(f"Existem {Numerosmedicos} com salario superior a 4.500,00")

