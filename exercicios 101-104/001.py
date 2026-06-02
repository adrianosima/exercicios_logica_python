"""
1. Crie um programa no qual o usuário informe 2 números inteiros: 
a e b. Para que o programa continue sua execução, verifique 
se a < b. Se sim, calcule a soma dos números inteiros no intervalo 
[a, b]. Caso contrário, informe uma mensagem de erro. 

"""

PrimeiroNumero = int(input("Escreva o primeiro numero inteiro: "))
SegundoNumero = int(input("Escreva o segundo numero inteiro: "))

SomaInterior = 0

if PrimeiroNumero < SegundoNumero:
    for i in range(PrimeiroNumero, SegundoNumero):
        if PrimeiroNumero < i < SegundoNumero:
            SomaInterior += i

    print(SomaInterior) 

else:
    print("Erro numero informado não compativel")
