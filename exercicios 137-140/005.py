"""

5. Crie um programa que declare uma lista L, a qual você pode 
preenchê-la manualmente. Em seguida, o programa deve cal
cular a média geométrica entre o menor e o maior elemento da 
lista L. Ao fim, o programa deve imprimir a média geométrica 
encontrada.

"""

listaNumero = []

while True:    
    Numeros = float(input('Escreva os numeros para preencher a lista: '))

    if Numeros == -1:
        maior = listaNumero[0]
        menor = listaNumero[0]
        
        for i in listaNumero:
            if i > maior:
               maior = i

            elif i < menor:
                menor = i

        print(f'maior numero é {maior}')
        print(f'Menor numero é {menor}')
        print(f'A média geométrica entre {maior} e {menor} = {(maior*menor)**(1/2)} ')
        
        break
    
    else:
        listaNumero.append(Numeros)
