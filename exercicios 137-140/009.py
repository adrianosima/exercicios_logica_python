lin = int(input("Número de linhas: "))
col = int(input("Número de colunas: "))
    
# Se matriz não é quadrada não pode ser triangular
if lin != col:
    print("Matriz não é triangular.")
else:
    M = []
    triangular = True 
    for i in range(lin):
        ELEM = []
        for j in range(col):
            ELEM.append(int(input(f"M[{i+1}][{ j+1}] = ")))
        M.append(ELEM)
   
    print("Matriz M:")
    for i in range(lin):
        for j in range(col):
            print(M[i][j], end='')
        print()
   
    for i in range(lin):
        for j in range(col):
            # Elemento acima da DP?
            if i < j:
            # Se algum elemento acima da DP é diferente de 0
            # M não pode ser tringular inferior
                if M[i][j] != 0:
                    triangular = False
                    break # Encerra a busca
    if triangular == True:               
        print("M é uma matriz triangular inferior.")
    else:
        print("M não é uma matriz triangular inferior.")