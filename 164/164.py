#variável que armazena o caminho do arquivo
nome_arquivo= 'pi.txt'

#variável que armazena o conteúdo do texto
texto=''

#com a função open nos criamos um objeto que representa o arquivo de texto
with open(nome_arquivo) as pi:
    #Lemos o conteudo e armazenamos em uma variávle para acessar fora do bloco
    lines= pi.readlines()

#loop que concatena o conteudo de cada linha em um única linha
for line in lines:
    texto += line.strip()

#imprimindo as primeiras 50 casas decimais do pi, 
print(texto[:52])

