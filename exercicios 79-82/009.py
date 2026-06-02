"""

9. Na última Black Friday, o gerente de uma loja de perfumes 
colocou todo o seu estoque em promoção, de acordo com a 
tabela a seguir:
 Código       Condição de Pagamento              Desconto (%)
 1            À vista (em espécie)                   15
 2            Cartão de débito                       10
 3            Cartão de crédito (vencimento)         5
 
Construa um programa que solicite ao operador do caixa o preço 
total da venda, bem como a forma de pagamento. Ao fim, o pro
grama deve informar o valor final a ser pago. 

"""

precoTOtalvenda = float(input("Escreva o preço total da venda: "))
print("Código       Condição de Pagamento")
print(" 1            À vista (em espécie) \n 2            Cartãodedébito\n 3            Cartão de crédito (vencimento)")
print("\n")
CondicaoPagamento = int(input("Informe a condição de pagamento: "))

if CondicaoPagamento == 1:
    descontos = ((precoTOtalvenda)-(precoTOtalvenda*15/100))
    print(descontos)
    
elif CondicaoPagamento == 2:
    descontos = ((precoTOtalvenda)-(precoTOtalvenda*10/100))
    print(descontos)

elif CondicaoPagamento == 3:
    descontos = ((precoTOtalvenda)-(precoTOtalvenda*5/100))
    print(descontos)

else: print("Não encontrado!")