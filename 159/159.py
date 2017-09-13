#com a funão open abrimos o arquivo de texto como um objeto chamado arquivo
with open('pi.txt.txt') as arquivo:
    #Aplicamos o método read emcima do objeto arquivo e assim armazenamos o resultado dentro de uma variável
    conteudo= arquivo.read()
    #imprimimos o resultado armazenado em conteúdo
    print(conteudo)
