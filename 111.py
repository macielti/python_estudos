#Definimos um dicionários com 3 listas dentro
pessoas = {
    'eutino' : [ 'java', 'c', 'python' ],
    'wanderson' : [ 'php', 'java', 'html', 'javascript' ],
    'bruno' : [ 'python', 'c', 'ruby' ],
}

#Loop para pegar a key e os valores a cada ciclo
for pessoa, linguagens in pessoas.items():
    #imprimo o nome da pessoa concatenda com uma string
    print( '\n' + pessoa.title() + " As suas liguagens preferidas são:")
    
    #Este segundo for pega a lista armazenada em cada keys e imprime 
    for linguas in linguagens:
        print("Linguagem: ", linguas)
