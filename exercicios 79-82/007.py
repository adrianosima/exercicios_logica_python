"""

 7. Crie um programa que solicite ao usuário a informação de 3 estaturas. 
Caso existam estaturas iguais, o programa deve apresentar 
a mensagem “Há, pelo menos, 2 pessoas com a mesma estatura”. 
Caso contrário, o programa deve informar a maior estatura.

"""

estaturas1 = float (input("Escreva a primaira estatura: "))
estaturas2 = float (input("Escreva a segunda  estatura: "))
estaturas3 = float (input("Escreva a terceira estatura: "))

if (estaturas1 == estaturas2 == estaturas3):
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

elif ((estaturas2 == estaturas3) or (estaturas1 == estaturas2) or (estaturas1 == estaturas3) ):
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

elif ((estaturas1 > estaturas2) and (estaturas1 > estaturas3)):
    print(estaturas1)

elif ((estaturas3 > estaturas1) and (estaturas3 > estaturas2)):
    print(estaturas3)


elif ((estaturas2 > estaturas1) and (estaturas2 > estaturas3)):
    print(estaturas2)

else: print("Não existente ")
