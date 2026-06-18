'''
1. Um usuário do departamento de vendas de uma empresa necessita
de um relatório que apresente seus clientes potenciais. 
Para isso, é necessário que o relatório seja ordenado do cliente que mais comprou para o que menos comprou. Os dados de 
entrada são razão social e valor total de compras. Considere a 
razão social como sendo a chave identificadora do cliente.

'''

relatorio = {}

while True:
    cadastro = {
        'razão_social':f'{input('Escrva a razão social')}',
        'valor_total_conpras': float(input('Escreva o valor total das vendas: '))

    }
    parar = input('pretendes parar [N/S]')

    if (parar.lower() == 'n'):
        print(relatorio)
        break

    else:
        relatorio.update(cadastro)
        continue