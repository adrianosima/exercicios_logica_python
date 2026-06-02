"""
4. Implemente um programa que converta o valor de uma velocidade média em km/h 
para m/s. Para isso, o usuário deve informar o valor da velocidade média. 
Sabe-se que o fator utilizado para essa conversão é 3,6.
"""
print("*"*50)
VelocidadeMedia = float(input("Escreva o valor da velocidade média em km/h: "))
print("*"*50)
print("Velocidade Média km/h | Velocidade Média m/s")
print("*"*50,"*")
print(f"{VelocidadeMedia}km/h",""*49 ,f" | {VelocidadeMedia*3.6}")
print("*"*50)