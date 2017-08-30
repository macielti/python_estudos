#Defini uma função que recebe tres parâmetros onde o terceiro é opcional
def name(prim, ult, second_name=''):
    
    #O if verifica se o terceiro parâmetro foi preenchido
    if second_name:
        complete = prim + ' ' + ult + ' ' + second_name
    
    #Caso o terceiro parâmetro esteja vazio
    else:
        complete = prim + ' ' + ult
    
    #Retorna o resultado do processamento das entradas da  função
    return complete.title()
    
#Lista onde serão armazenados os resultados da função
lista=[]

#Armazena o resultado da função nos dois casos com e sem o terceiro parametro
#dentro da lista
lista.append(name('bruno', 'nascimento'))    
lista.append(name('bruno', 'nascimento', 'maciel'))

#Loop para imprimir a lista com os resultado
for name in lista:
    print(name.title())
