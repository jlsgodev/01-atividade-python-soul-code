'''
7.2. Crie uma nova tupla concatenando a tupla do exercício anterior com o e-mail
do cliente. Imprima a nova tupla.
'''

cliente = ("jhon",32, 82, 1.79)
mail = "jhon@mail.com"

cliente = cliente + (mail,)

print(cliente)