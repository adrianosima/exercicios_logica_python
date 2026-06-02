"""

3. Construa um programa que receba o nome e o preço de 5 
medicamentos de uma drogaria (considere que o usuário 
informou cinco medicamentos distintos). O programa deve 
informar o nome e o preço do medicamento mais barato, 
bem como a média aritmética dos preços informado

"""
import statistics

Cont = 0
Preco = []
Medica = []

while Cont != 5:
    Medicamentos = input("Escreva o nome do medicamento: ")
    PrecoMedicamentos = float(input("Escreva o presso do medicamento: "))
    Cont += 1
    Preco.append(PrecoMedicamentos)
    Medica.append(Medicamentos)
    
    if Cont == 5:
        Media = statistics.mean(Preco)
        Precobaixo = min(Preco)
        posissao = int(Preco.index(Precobaixo))

print(f"O medicamento mais barato é {Medica[posissao]} o seu preço {Precobaixo} a media entre os medicamentos é {Media}")
        