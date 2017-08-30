#Defini uma função que recebe três parametros. O ultimo, a idade é opcional
def informs(nome, segundo, idade=''):
    
    #Neste caso ele cria o dicionario com as informações do parametro, sem a
    #idade
    informacoes={'nome' : nome.title(), 'segundo_nome' : segundo.title(),}
    
    #Condicional para se a idade for preenchida então a informação do parâmetro
    #é passada para o dicionario
    if idade: 
        informacoes['idade'] = idade
    
    #retorna o dicionario
    return informacoes
    
#Chamo a função com o parametro idade e armazeno o resultado em uma var e dipois
#imprimo o resultado    
informacoes = informs('bruno', 'nascimento', '12')
print(informacoes)    

#Chamo a função sem passar a idade e imprimo o resultado
informacoes = informs('bruno', 'nascimento')
print(informacoes)
