"""

 4. Suponha que o professor Fábio possui 2 logins na rede acadêmica da instituição. 
Construa um programa que valide o acesso do professor à rede. 
Caso o par usuário/senha informado esteja correto, 
o programa deve imprimir a mensagem “Seja bem vindo!”. 
Caso contrário, “Usuário e senha não conferem”.
    login 1
        usuário: procopio     
        senha: 12345
    login 2
        usuário: paiva     
        senha: 54321
"""

usuário1 = "procopio"     
senha1 =  12345

usuário2 = "paiva"     
senha2 = 54321

nomeusuario = input("Escreva o nome de usuário: ")
senhadigitada = int(input("Escreva a sua senha: "))

if ((usuário1 == nomeusuario) and (senha1 == senhadigitada)):
    print("Seja bem vindo")

elif ((usuário2 == nomeusuario) and (senha2 == senhadigitada)):
    print("Seja bem vindo")

else: print("Usuário e senha não conferem")

