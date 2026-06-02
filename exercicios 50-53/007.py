"""
7. Uma imobiliária paga aos seus corretores um salário 
base de R$ 1.500,00. Além disso, uma comissão de R$ 
200,00 por cada imóvel vendido e 5% do valor de cada 
venda. Construa um programa que solicite o nome do 
corretor, a quantidade de imóveis vendidos e o valor 
total de suas vendas. Ao fim, o programa deve calcular 
e escrever o salário final do corretor de imóveis.
"""
SalarioBase = 1500
imovelvendido = 200

NomeCorretor = input("Escreva o seu nome: ")
QuantidadeImovelVendido = int(input("Escreva a quantidade de imavel vendidos: "))
ValorTotalVendas = float(input("Escreva o valor total da vendas: "))

SalarioFinal = (SalarioBase + (imovelvendido*QuantidadeImovelVendido) + (((5*4)/100)*ValorTotalVendas))

print(f"{NomeCorretor} o teu salario {SalarioFinal} R$")
