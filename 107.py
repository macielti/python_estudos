# Defini 3 dicionários 
player1 = {
    'color' : 'blue',
    'pontuacao' : 20, 
}

player2 = {
    'color' : 'red',
    'pontuacao' : 35,
}

player3 = {
    'color' : 'green',
    'pontuacao' : 15,
}

#armazenei esses dicionários dentro da lista players
players = [ player1, player2, player3 ]

#com o for eu pego cada item da lista, no caso cada dicionário, e imprimo cada um deles
for jogador in players:
    print(jogador)
    
# Estou me aprofundando mais na legibilidade do código, esse deve estar mais legível que os anteriores
