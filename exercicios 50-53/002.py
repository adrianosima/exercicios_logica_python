from math import pi
import time

"""
2. Agora o mesmo aluno precisa que você construa um programa 
para calcular o comprimento de uma circunferência. Para 
isso, o aluno informará ao programa o raio da circunferência. 
Sabe-se que Comp_circ = 2pir                        
"""
Raio = float(input("Escreva o valor do raio: "))

Comp_circ = 2*pi*Raio
print(f"O comprimento da circunferancia de raio {Raio} é igual a {Comp_circ}")

time.sleep(3)
