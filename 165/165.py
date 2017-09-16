#nome do arquivo armazenado em um variável
filename= 'pi.txt'

#variável para armazenar cada linha concatenada em um única
concatenado=''

#com a funão open criamos um objeto que representa o arquivo de texto
with open(filename) as pi:

    #variável que armazena a lista de linhas para acesso fora do bloco
    text= pi.readline()

#loop que concatena cada linha em uma só
for line in text:
    concatenado += line.strip()

#variável que armazena as primeiras 50 casas decimais do numero pi
casas_50= concatenado[:52]

#entramos com a data de aniversário da pessoa
data= input('Digite a sua data de aniversário no formato ddmmaa:')

#se a data de aniversário estiver nas 50 primeiras casas decimais agente imprime
#uma mensagem que indica isso, e caso contrário agente imprime uma menságem
#negativa 
if  data in casas_50:
    print('A sua data de aniversário aparece nas primeiras 50 casas dacimais')
else:
    print('A sua data de aniversário não aparece nas primeiras 50 casas\
 decimais')
