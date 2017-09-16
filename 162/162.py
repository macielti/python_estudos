#nome do arquivo armazenado em uma variável
file_name= 'pi.txt'

#com a função open, definimos um objeto chamato pi que representa o arquivo de
#texto
with open(file_name) as pi:
   
    #armazeno a lista de linhas do arquivo em uma varável para acesso fora do 
    #bloco
    list_lines= pi.readlines()

#loop para imprimir cada linha do arquivo removendo as linas em branco com o
#rstrip()
for line in list_lines:
    print (line.rstrip())
