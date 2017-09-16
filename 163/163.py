#variável para armazenar o caminho do arquivo
file_name= 'pi.txt'

#declaração de variáveis 
text=''
texto=''

#Criamos um objeto que representa o arquivo
with open(file_name) as pi:
    
    #armazenamos as linhas do arquivo em uma variavel
    text= pi.readlines()

#o loop pega cada linha, retira os espaços e concatena dentro da variável texto
for line in text:
    texto += line.strip()

#imprimimos o texto
print(texto)
#imprimimos a quantidade de caracteres do arquivo
print(str(len(texto))+' caracteres')
