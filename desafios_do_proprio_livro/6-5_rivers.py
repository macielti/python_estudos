rivers={
    'nile':'egypt',
    'amazonas':'brazil',
    'yangtzé':'china',
}

for rios, pais in rivers.items():
    print('The '+rios.title()+' through '+pais.title())
    
for rio in rivers.keys():
    print(rio.title())

for pais in rivers.values():
    print(pais.title())
