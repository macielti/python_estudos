#Criamos um dict vazio
responses = {}

#Loop infinito
while True:

    #Lemos o nome e a montanha e armazenamos em suas respectivas variaveis
    nome = input('\nQual é o seu nome?')
    mont = input('\nQuam montanha você gostaria de escalar?')

    #Adicionamos uma chave ao dict chamada o nome que a pessoa entrou com o valor da montanha
    responses[nome] = mont
    
    #Pergunta ao user se tem mais alguem
    option = input('\nMais alguem quer resposnder? ("sim" ou "não")?')

    # se a opção for não ele encerra o loop e pula pros resultados
    if option == 'não':
        break

#anuncia os resultados
print('--resultas da enquete--\n')

#Com o for exibimos cada chave com o seu valor em um print contatenado com strings
for  keys, values in responses.items():
    print(keys.title() + ' gostaria de escalar no ' + values)
