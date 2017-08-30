#Váriável booleana rebendo o valor Verdadeiro
valor_de_verdade= True

#Loop infinito, uma vez que o valor verdade sempre será verdadeiro
while valor_de_verdade == True:

        #Usuária entra com uma idade ou comando para sair
        entrada = input('\nDigite a tua  idade, que descobrirei a rua idade: (digite "sair" para sair)')

        #Se ele digitar 'sair' o loop é interrompido, podemos interromper um loop infinito com o comando break
        if entrada == 'sair':
            break
        
        #Se ele não tiver digitado sair eu retorno de alguma forma o que ele digitou
        else:
            print('\nA tua idade é ' + entrada+ ' anos')
