'''
Contexto:
Uma escola precisa analisar as notas de seus alunos e determinar se cada aluno
foi aprovado ou reprovado. As notas serão armazenadas em uma lista e a análise
deve ser realizada em um loop.
'''

'''
Requisitos:
Peça ao usuário para inserir o nome e a nota de cinco alunos.
Armazene os nomes e as notas em listas separadas.
Para cada aluno, verifique se a nota é maior ou igual a 60. Se sim, o aluno está
aprovado; caso contrário, está reprovado.
Exiba uma mensagem para cada aluno informando seu nome, nota e se foi aprovado
ou reprovado.
'''

alunos = []
notas = []
for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    nota =  int(input("Digite a nota do aluno: "))
    alunos.append(aluno)
    notas.append(nota)

for i in range(5):
    if notas[i] >= 60:
        print("O aluno", alunos[i],   "foi aprovado!  Com a nota : ", notas[i])
    else: 
        print("O aluno", alunos[i], "foi reprovado! com a nota : ", notas[i])




