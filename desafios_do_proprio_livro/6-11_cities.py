cities={
    'gilbués':{
        'pais':'brasil',
        'população':10393,
        },
    'corrente':{
        'pais':'brasil',
        'população':15693,
        },
    'monte alegre':{
        'pais':'brasil',
        'população':55459,
        },
}

for key, value in cities.items():
    print(key.title()+': ')
    for chave, valor in value.items():
        print(chave.title()+': '+str(valor))
    print('\n')
