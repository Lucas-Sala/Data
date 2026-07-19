pessoa = {
    'nome' : 'Lucas',
    'idade' : 24,
    'altura' : 1.89
}

print(type(pessoa))

pessoa['peso'] = 100

print(pessoa)

print(pessoa.keys())

print(len(pessoa))

pessoa.pop('idade')

print(pessoa.get('nome'))

for v in pessoa.values():
    print(v)