languages={
    'samoel':'C',
    'wanderson':'PHP',
    'eutino':'Java',
    'bruno':'python',
}
friends=['wanderson','rafael','bruno']
for name in languages.keys():
    print('\n'+name.title())
    if name in friends:
        print('Linguagem de programação: '+languages[name]+'\n' )
# na linha 1 eu defini um dicionário;
#na linha 7 eu defini uma lista;
# na linha 8 eu criei um for para que em cada ciclo eu tenha o nome de uma pessoa na var name;
# na linha 9 eu imprimo todos os nomes das chaves sem os seus valores usado a função keys;
#na linha 10 eu criei uma codição para ser executada apenas quando o nome do amigo estiver dentro da lista;
#na linha 11 eu imprimo o valor da chave, que é a linguagem.