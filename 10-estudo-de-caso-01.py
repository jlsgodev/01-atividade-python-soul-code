

"""
Contexto:
Uma empresa precisa registrar informações sobre seus clientes e calcular o IMC
(Índice de Massa Corporal) de cada um deles. As informações devem ser
armazenadas em um dicionário e exibidas ao final.
"""


"""
Requisitos:
Peça ao usuário para inserir os seguintes dados de um cliente:
Nome
Idade
Peso (em kg)
Altura (em metros)
E-mail
Armazene essas informações em um dicionário.
Calcule o IMC do cliente (IMC = Peso / (Altura * Altura)) e adicione esse valor ao dicionário.
Exiba todas as informações do cliente, incluindo o IMC arredondado para duas casas decimais.

"""


nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso do cliente: "))
altura = float(input("Digite o altura do cliente: "))
email = input("Digite o email do cliente: ")

cliente = {"Nome": nome,"Idade": idade,"Peso": peso,"Altura": altura,"Email": email}



imc = peso / (altura * altura )
imc =round(imc,2)

cliente["IMC"] = imc



print(cliente)



