'''
5.2. Peça ao usuário para digitar uma frase e:
Converta a frase para maiúsculas.
Converta a frase para minúsculas.
Converta a primeira letra de cada palavra para maiúscula.
Verifique se a frase começa com uma determinada palavra (ex.: 'Olá').
'''


frase =  input("Digite uma frase: ")

print(frase.upper())
print(frase.lower())
print(frase.title()) 
print(frase.count("hello"))