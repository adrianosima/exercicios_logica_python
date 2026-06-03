"""
8. Crie um programa no qual o usuário informe o número de 
linhas e o número de colunas de uma matriz M e, em seguida, 
o usuário deve digitar os elementos de M. Ao fim, o programa 
deve informar se M é uma matriz identidade.]

M = [ 1, 0, 0
      0, 1, 0
      0, 0, 1
      ]
"""

lin = int(input("Esceva o número de linhas: "))
col = int(input("Esceva o número de col: "))

if lin != col:
    print("Não é unidade")

else:
    M = []

    for i in range(lin):
        Elem = []
        for j in range(col):
            Elem.append(int(input(f"M[{i+1}][{j+1}] = ")))

        M.append(Elem)
    print(M)
