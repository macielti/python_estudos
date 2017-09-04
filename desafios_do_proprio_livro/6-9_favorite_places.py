favorite_places={
    'bruno ribeiro':['verdão'],
    'luiz henrique':['verdão', 'rodoviária'],
    'tiago gonçalves':['mato', 'universidade aberta','fausto lustosa'],
}

for key, valor in favorite_places.items():
    print(key.title()+': ')
    for val in valor:
        print(val.title())
    print('\n')
