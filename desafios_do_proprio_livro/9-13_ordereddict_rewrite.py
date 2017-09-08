from collections import OrderedDict 

glossary= OrderedDict()

glossary['print']= 'Imprime uma string na tela'
glossary['str()']= 'Converter um número para string'
glossary['title()']= 'Pega a primeira letra de cada palavra e coloca maiuscula'
glossary['if']= 'Tomada de decisão'
glossary['return']= 'Saida de uma função'
glossary['keys()']= 'Cria uma lista com as chaves dos dicionários.'
glossary['items()']= 'Cria uma lista com os valotes das chaves do dicionario.'
glossary['class']= 'Cria uma classe'
glossary['for']= 'Serve para fazer loops'
glossary['while']= 'Outra forma de fazer loops'


for keyword, meanig in glossary.items():
    print(keyword+': '+ meanig)
