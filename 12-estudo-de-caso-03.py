# Contexto
# Uma empresa deseja realizar uma pesquisa de opinião com cinco participantes
# sobre um novo produto. As respostas devem ser armazenadas e analisadas para
# verificar a satisfação dos clientes.

# Requisitos
# Peça ao usuário para inserir o nome e a opinião (satisfeito/insatisfeito) de
# cinco participantes.
# Armazene os nomes e as opiniões em um dicionário.
# Conte o número de participantes satisfeitos e insatisfeitos.
# Exiba a lista de participantes satisfeitos e insatisfeitos, bem como o número
# total de cada categoria.

participantes = {}
satisfeitos = 0
insatisfeitos = 0

for i in range(5):
    nome = input("Digite o  nome do participante:  ")
    opiniao = input("Digite a  opinião do participante. (satisfeito/insatisfeito):  ")
    participantes[nome] = opiniao

for opiniao in participantes.values():
    if opiniao == "satisfeito":
        satisfeitos += 1
    elif opiniao == "insatisfeito":
        insatisfeitos += 1

print("Total de participantes satisfeitos:",  satisfeitos)
print("Total de participantes insatisfeitos:",  insatisfeitos)

print("Lista de participantes satisfeitos:")
for nome, opiniao in participantes.items():
    if opiniao == "satisfeito":
        print(nome)

print("Lista de participantes insatisfeitos: ")
for nome, opiniao in participantes.items():
    if opiniao == "insatisfeito":
        print(nome)



