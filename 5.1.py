'''
5.1. Peça ao usuário para digitar um e-mail e verifique se o e-mail contém o
caractere '@'. Imprima uma mensagem indicando se é um e-mail válido ou não.
''' 
# Métodos de Strings 

mail = input("Digite seu Email: "  )

if  ("@" in mail):
    print("Email Valido!")
else:
    print("Email invalido!")