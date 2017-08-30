#Função que recebe dois parametros
def dicionario(first,last):

    #Armazena os parametros dentro de um dicionario
    userinfo={'primeiro':first.title(), 'ult':last.title()}
    
    #Retorna um dicionario
    return userinfo

#Imprime o resultado da função
print(dicionario('bruno', 'do nascimento maciel'))
