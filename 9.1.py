# Condicionais
'''
9.1. Peça ao usuário para digitar sua idade e verifique se ele é menor de idade,
 adulto ou idoso. Imprima uma mensagem correspondente.
'''





idade = int(input("Digite sua idade :  "))
if (idade <= 17):
    print("Você é menor de idade")
elif (idade >= 18 and idade <= 60):
    print("Você é maior de idade")
else:
    print("Você é idoso")


