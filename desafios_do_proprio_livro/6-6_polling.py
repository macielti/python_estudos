favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

lista=['jen', 'bruno', 'sarah']

for pessoa in lista:
    if pessoa in favorite_languages:
        print(pessoa.title()+' já respondeu a pesquisa')
    else:
        print(pessoa.title()+' por favor responda a pesquisa') 
