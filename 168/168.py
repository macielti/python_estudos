#nome do arquivo armazenado em uma variavel
filename= 'message.txt'

#lista de mensagens a serem anexadas
list_message= ['Olá  mundo.', 'I love Python.']

#loop que anexa as mensagems ao arquivo
for message in list_message:
    
    #abro e escrevo a mensagem no arquivo
    with open(filename, 'a') as menss:
        menss.write(message+'\n')
