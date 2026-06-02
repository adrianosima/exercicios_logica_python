"""

4. Imagine um sistema de caixa eletrônico. Construa um pro
grama que receba a senha de um correntista para validar o seu 
acesso ao sistema. Considere que a senha fictícia do correntista 
é 123456. Considere as seguintes restrições:
    • quando a senha estiver correta, mostrar a mensagem: 
“Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
    • quando o usuário errar a senha pela primeira vez, 
mostrar a mensagem: “Senha incorreta! Você ainda 
tem 2 tentativas.”
    • se o usuário errar a senha pela segunda vez, mostrar 
a mensagem: “Senha incorreta! Você ainda tem 1 ten
tativa.”
     • se o usuário errar a senha novamente, mostrar a men
sagem “Sua senha foi bloqueada! Por favor, dirija-se a 
um de nossos caixas.” e o programa deve ser encerrado.

"""

TentativaSenha = 3
NomeCorretor = input("Informe o seu nome: ")

for i in range(3):
    DigitaSenha = int(input("Escreva a sua senha: "))
    TentativaSenha-=1

    if DigitaSenha == 12345:
        print(f"Olá, {NomeCorretor}. Seja bem-vindo ao nosso banco!")
        break
    
    elif TentativaSenha == 0:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas")
        break

    elif DigitaSenha != 12345:
        print(f"Senha incorreta! você ainda tem {TentativaSenha} Tentativas")

    

    

