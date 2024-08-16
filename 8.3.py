'''
8.3. Remova a chave 'peso' do dicionário e verifique se a chave 'endereço' está
no dicionário. Imprima os resultados.
'''

pessoa = {
    "nome": "jhon",
    "idade": 32,
    "peso": 82,
    "cidade": "BC",
    "email": "jhon@mail.com"
}


pessoa.pop("peso")

print(pessoa)

if "endereco" in pessoa:
    print(pessoa["enereco"])


