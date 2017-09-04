uauau={
    'kind':'dog',
    'name':'bruno',
}
gerry={
    'kind':'caracol',
    'name':'jefferson',
}
xaninho={
    'kind':'gato', 
    'name':'manin'
}

pets=[uauau, gerry, xaninho]

for pet in pets:
    for k, v in pet.items():
        print(k.title()+': '+v.title())
    print('\n')
