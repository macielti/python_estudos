#Defini um dicionário com uma lista dentro dele
pizza = {
    'tipo' : 'sem fatiar',
    'coberturas' : [ 'queijo', 'tomate', 'ovo', 'frango' ]
}

#printei  uma string concatenada com o tipo da pizza


# Usando o for e o if eu peguei apenas a key de coberturas e imprimi  elas
for keys, values in pizza.items() :
    
    # quando a key for tipo então o valor dela é o tipo da piza
    if keys == 'tipo':
        print( "Tu pediste uma Pizza " + values, "com as sequintes coberturas:" )
    
    #quando o key não for tipo, então são as coberturas
    else:
        
        # pego cada elemento da lista de coberturas e imprimo pro user
        for ID_COBERT in values :
            print('\t=>', ID_COBERT.title() )
            
