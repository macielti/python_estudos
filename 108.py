#Defini uma lista Vazia
players = [ ]

# Usei um loop para gerar 30 jogadores e armazenar esses jogadores(dicionários) dentro de uma lista
for player_num in range(1, 31) :
    player = {
        'cor' : 'azul',
        'pontos' : 40,
        'velocidade' : 130,
    }
    players.append(player)

# usando o fatiamento com binado com o loop, passamos os 5 primeiros elementos para a variável dicts, e printei
for dicts in players[ : 5 ] :
    print( dicts )

# usando o função len exibi o comprimento da lista, e a função str converteu o valor retornado pela função len para uma string
print( "Número de jogadores é " + str( len(players) ) )
