#Defini uma lista Vazia
players = [ ]

# Usei um loop para gerar 30 jogadores e armazenar esses jogadores(dicionários) dentro de uma lista
for player_num in range(1, 31) :
    
    # se for um dos tres primeiros elementos ele define os valores abaixo para o dictionario
    if player_num <= 3:
        player = {
            'cor' : 'red',
            'pontos' : 60,
            'velocidade' : 150,
        }
    # para o resto dos elementos ele define esses valores abaixo
    else:
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
