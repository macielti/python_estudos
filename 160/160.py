#armazeno o caminho do arquivo em um variavel
file_name= 'pi.txt'

#Com a função open nos criamos um objeto que representa  arquivo.
with open(file_name) as pi:
    
    #loop que imprime cada linha do arquivo
    for line in pi:
        print (line)
