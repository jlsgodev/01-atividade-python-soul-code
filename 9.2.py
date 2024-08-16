# Condicionais
'''
9.2. Peça ao usuário para digitar uma nota (0 a 100) e imprima se ele foi
aprovado (nota >= 60) ou reprovado.
'''

nota = int(input("Digite sua nota da prova: "))
if (nota >= 60 and nota <= 100):
    print("Você foi aprovado")
elif (nota >= 0 and nota <= 59):
    print("Você foi reprovado")
else:
    print("Valor inválido")