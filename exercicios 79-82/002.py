"""
2. Construa um programa que solicite ao usuário dois números 
positivos. Em seguida, o programa deve apresentar o seguinte 
menu:

    1. Média ponderada, com pesos 2 e 3, respectivamente
    2. Quadrado da soma dos 2 números
    3. Cubo do menor número

    Escolha uma opção: 
De acordo com a opção informada, o programa deve calcular a 
operação apresentada no menu. Se a opção escolhida for inváli
da, o programa deve mostrar a mensagem “Opção inválida” e ser 
encerrado. 
"""

NumeroPrimeiroPositivos = float(input("Informe o primeiro número positivo: "))
NumerosSegundoPositivos = float(input("Informe o Segundo número positivo: "))

if ((NumeroPrimeiroPositivos )>0 and (NumerosSegundoPositivos)>0):

    print("*"*60)
    print("|                               Menu                       |")
    print("*"*60) 
    print("| * 1. Média ponderada, com pesos 2 e 3, respectivamente   |")
    print("*"*60)
    print("| * 2. Quadrado da soma dos 2 números                      |")
    print("*"*60)
    print("| * 3. Cubo do menor número                                |")
    print("*"*60)

    EscollhaOpecao = int(input("Escolha a tua opção: "))
    
    if EscollhaOpecao == 1:
        MediaPonderada = (NumeroPrimeiroPositivos*2 + NumerosSegundoPositivos*3)/(5) 
        print (MediaPonderada)

    elif EscollhaOpecao == 2:
        print("*"*60)
        print(f"| * 2. Quadrado da soma dos 2 números            | {(NumeroPrimeiroPositivos+NumerosSegundoPositivos)**2} |")
        print("*"*60)

    elif EscollhaOpecao == 3:
        if NumeroPrimeiroPositivos < NumerosSegundoPositivos: 
            print("*"*60)
            print(f"| * 3. Cubo do menor número                          {NumeroPrimeiroPositivos**3}|")
            print("*"*60)

        else:
            print("*"*60)
            print(f"| * 3. Cubo do menor número                          |     {NumerosSegundoPositivos**3}|")
            print("*"*60)

    else:
        print("Opção inválida")  

elif ((NumeroPrimeiroPositivos < 0 ) or (NumerosSegundoPositivos < 0)) :
    print("Enforme apenas valores positivos")
