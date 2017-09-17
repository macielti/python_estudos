#armazenamos o nome do arquivo
filename= 'rodrigo.txt'
#tentamos abrir o arquivo e imprimir o seu conteúdo
try:
    with open(filename) as rod:
        conteudo= rod.readlines()
        print(conteudo)
#caso ocorra erro, imprima uma mensagem personalisada
except FileNotFoundError:
    print('O arquivo '+filename+' não existe.')
