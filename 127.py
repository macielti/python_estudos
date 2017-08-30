#Lista com algus elementos repetidos
memes = ['carro_pica', 'jamelão', 'galo_cego', 'jamelão', 'guina']

#imprimindo a lista
print(memes)

#Loop para verificar se o elemento contem jamelao
while 'jamelão' in memes:

    #se o elemento contem jamelão, ele é removido da lista
    memes.remove('jamelão')

#imprimimos a lista depois da remoção dos elementos repetidos    
print(memes)
