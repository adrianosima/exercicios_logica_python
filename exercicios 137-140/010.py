#iniciante intermedio
#siga para mais videos

numero1 = float(input("Escreva o primeiro numera: "))

operador =input("Escreva o operador: ")

numero2 = float(input("Escreva o segundo numera: "))

if operador == '+':
    cal = numero1 +numero2

elif operador == '-':
    cal = numero1 -numero2

elif operador == '*':
    cal = numero1 *numero2

elif operador == '/':
    cal = numero1 /numero2

else:
    print("operador não encontrado")

print(f'{numero1} {operador} {numero2} = {cal}')