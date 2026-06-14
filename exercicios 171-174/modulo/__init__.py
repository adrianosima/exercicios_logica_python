from time import sleep
from math import pi


def Menu():
    print("Calculo da area de figuras geométricas:")
    sleep(1)

    print(" 1.Círculo")
    sleep(1)
    print(" 2.Triângulo")
    sleep(1)
    print(" 3.Retângulo")
    sleep(1)



def triangulo(h, b):
    A = (b*h)/2
    return A     


def retangulo(b, h):
    A = b*h
    return A

def circulo(r):
    A = pi*(r**2)
    return A