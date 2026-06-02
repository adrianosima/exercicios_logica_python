"""

6. Em seu programação semanal, uma rede de televisão apresenta 
os seguintes telejornais:
    • Bom Dia Nação, apresentado por Zé PINHEIRO e por 
    Ana Carla ARAÚJO
    • Jornal Brasileiro, apresentado por Bill BONNER E 
    CARLA VASCONCELOS
Crie um programa no qual o usuário informe o sobrenome de um 
dos apresentadores. Se o sobrenome informado não estiver na 
lista acima, o programa deve mostrar a mensagem “Apresenta
dor(a) desconhecido(a).”. Em caso positivo, o programa deve mostrar 
o nome do telejornal apresentado pelo apresentador(a).

"""

sobrenome = input("Escreva o sobrenome do apresentado:")

sobrenome.strip().upper()

if (sobrenome == "PINHEIRO" or sobrenome == "ARAÚJO"):
    print("Bom Dia Nação")

elif (sobrenome == "VASCONCELOS" or sobrenome == "BONNER"):
    print("Jornal Brasileiro")

else:
    print("Apresentador(a) desconhecido(a).")
    