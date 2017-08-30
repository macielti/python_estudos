#Defini uma função que recebe dois argumentos
def pessoa(primeiro, segundo):

    #Variaveel recebe a concatenação desses dois parametros
    nome_complet= primeiro+' '+segundo
    
    #Retornamos variavel 
    return nome_complet

#Loop infinito
while True:

    #Leio os dois parametros para jogar dentro da função
    first = input('Digite o primeiro nome:')
    second = input('Digite o segundo nome:')
    
    #chamo a função e armazeno o resultado da função em uma variavel
    complet_nome = pessoa(first, second)
    
    #if onde se uma dos parametros for igual a 'q' o loop é interrompido
    if first == 'q' or 'q' == second:
        break;
    
    #Imprimo o resultado armazenado na variavel
    print(complet_nome.title())

