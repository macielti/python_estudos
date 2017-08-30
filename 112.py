# Defini um dicionário
pessoas = {

    #um outro dicionário dentro do outro
    'zuleide' : {
        'primeiro_name' : 'maria',
        'ult_name' : 'zuleide da silva',
        'loc' : 'alagoinnha', 
    },
    
    #mais um dicionario dentro do outro
    'galo_cego' : {
        'primeiro_name' : 'daniel',
        'ult_name' : 'orivaldo da silva',
        'loc' : 'nada ver'
    },
    
}

#For para pegar os items dos dicionários
for dicto, infos  in pessoas.items() :
    #passar o nome dos dicionário internos
    print(dicto + ':')

    #Imprimir os valores das keys internas e concatenar com strings
    print('Nome Completo: ' + (infos['primeiro_name'] + ' ' + infos['ult_name']).title())
    print('Localização: ' + (infos['loc']).title())
