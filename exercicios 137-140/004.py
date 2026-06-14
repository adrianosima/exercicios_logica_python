"""

4. Crie um programa que solicite o usuário um número N ímpar maior que 1. Em seguida, preencha uma lista com N números inteiros positivos (suponha que o usuário sempre digitará números inteiros positivos). Selecione o elemento que está no centro da lista. Ao final, calcule e escreva o 
fatorial do elemento selecionado.

"""
from modulo import factorial
from statistics import mean


NumeroImparNatural = int(input("Escreva um numero impar positivo: "))
NNatual = []

if ((NumeroImparNatural%2 != 0) and (NumeroImparNatural > 1)):
    for i in range(1,NumeroImparNatural+1):
        NNatual.append(i)
        CentroLista = mean(NNatual)
        
    factorial(CentroLista)

elif (NumeroImparNatural%2 == 0 and NumeroImparNatural > 0):

    print("digite um numero impar positivo")

elif ( NumeroImparNatural < 0):
    print("digite um numero impar positivo")


else:
    print("Valor invalido")
