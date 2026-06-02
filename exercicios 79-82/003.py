"""

3. Construa um programa que apresente para o usuário o menu 
abaixo:
**** TABELA VERDADE ****
    1.Operador AND
    2.Operador OR 
    3.Operador NOT 
************************** 
Escolha uma opção:
 Se a opção escolhida for 1 ou 2, o programa deve solicitar que o 
usuário informe 2 bits e, no caso da opção ser 3, o programa deve 
solicitar que o usuário informe apenas 1 bit. Ao fim, o programa 
deve usar o(s) bit(s) informado(s) e apresentar o resultado da 
operação selecionada, com base, na tabela verdade
"""

print("**** TABELA VERDADE ****")
print(" 1.Operador AND\n 2.Operador OR\n 3.Operador NOT")
print("**************************")

opcao = int(input("Escreva o número da opção: "))

if ((opcao == 1)):
    print("os bits são escritos em binario (0 ou 1): ")
    bit1 = int(input("informe o 1 bit: "))
    bit2 = int(input("informe o 2 bit: "))

    if (((bit2 == 0) and (bit1 == 1)) or ((bit1 == 0) and (bit2 == 1))):
        print(False)

    elif (((bit2 == 0) and (bit1 == 0)) or ((bit1 == 1) and (bit2 == 1))):
        print(True)

    

    else: print("Opção não encontrada")

elif ((opcao == 2)):
    print("os bits são escritos em binario (0 ou 1): ")
    bit1 = int(input("informe o 1 bit: "))
    bit2 = int(input("informe o 2 bit: "))

    if (((bit2 == 0) or (bit1 == 1)) or ((bit1 == 0) or (bit2 == 1))):
        print(True)

    else: print("Provavelmente um deles não é um bit")


elif opcao == 3:
    print("os bits são escritos em binario (0 ou 1): ")
    bit1 = int(input("informe 1 bit: "))
    if ( bit1 == 0):
        print("1")
    elif (bit1 == 1):
        print("0")    
    else:
        print("bit enexistente")

else:
    print("Opção não encontrada")
