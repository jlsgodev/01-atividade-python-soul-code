'''
3.2. Peça ao usuário para digitar sua idade, peso e altura. Calcule o IMC e
imprima o resultado arredondado para três casas decimais.
'''

idade = int(input("Digite sua idade: "))

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = (peso / (altura ** 2))
imc = round(imc, 3)
print("Seu IMC é: ", imc )