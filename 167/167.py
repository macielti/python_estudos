#nome do arquivo em uma variável
filename= 'message.txt'

#coma função open nos criamos um objeto que representa o arquivo
with open(filename, 'w') as message:
    
    #Escrevo uma mensagem no arquivo
    message.write('I love you Programming.')
    #com o \n quebramos a linha e escrevemos outra mensagem.
    message.write('\nI love Python.')
    
    
