#variável para armazenar o caminho para o arquivo
filename='txt.txt'

def count_words(filename):
    """Esta função conta a quantidade de palavras que tem no arquivo e exibe na\
tela"""
    #tentamos abrir o arquivo de texto para separar as palavras em uma lista
    try:
        with open(filename) as f_obj:
            conteudo= f_obj.read()
            fatiado=conteudo.split()
    #caso ocorra erro é exibido uma mensagem personalizada
    except FileNotFoundError:
        print('O arquivo '+filename+' não foi encontrado ou não existe.')
    
    #caso não ocorra erro ele exibe a quantidade de palavras do texto
    else:
        print('O arquivo '+filename+' tem '+str(len(fatiado))+' palavras')
#chamada da função encima de um arquivo
count_words(filename)
