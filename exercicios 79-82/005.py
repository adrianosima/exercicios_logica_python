"""

5. Uma empresa concederá um aumento de salário aos seus 
funcionários, variável de acordo com o cargo, conforme a tabela 
abaixo:
    Cargo                            Aumento (%)
    Programador de Sistemas             30
    Analista de Sistemas                20
    Analista de Banco de Dados          15
Crie um programa que solicite ao usuário o salário e o cargo de 
um determinado funcionário. Na sequência, o programa deve calcular 
e imprimir o seu novo salário. Caso o cargo informado não 
esteja na tabela, o programa deve imprimir “Cargo inválido”.

"""

ProgramadorSistema = "Programador de Sistemas"
AnalistaSistema    = "Analista de Sistemas"
AnalistaBancoDados = "Analista de Banco de Dados"

print("Tabela de cargos aceites")
print(f"     {ProgramadorSistema}\n     {AnalistaSistema}\n     {AnalistaBancoDados}")
print("*"*46)
print("\n")
cargofuncionario =   input("Escreva o seu cargo: ")
salariofuncionario = float(input("Escreva o seu salário: "))

if  ProgramadorSistema == cargofuncionario:
    aumentosalario = (salariofuncionario*(30/100))+(salariofuncionario)
    print(f"Novo é {aumentosalario}")

elif AnalistaSistema == cargofuncionario:
    aumentosalario = (salariofuncionario*(20/100))+(salariofuncionario)
    print(f"Novo é {aumentosalario}")

elif AnalistaBancoDados == cargofuncionario:
    aumentosalario = (salariofuncionario*(15/100))+(salariofuncionario)
    print(f"Novo é {aumentosalario}")

else: print("Cargo inválido")
    
