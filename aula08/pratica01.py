produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 15
}

produto.pop("estoque")

produto['preco'] = 4000.00

print(produto['nome'])
print('R$', produto['preco'])
