#A função recebe duas strings como argumentos, e retorna duas mensagens usando 
#esses argumentos, o argumento name recebe um valor padrão
def animatizatron2000(kind, name = 'piloto'):
    print("Eu tenho um "+kind+"!")
    print("O nome do meu "+kind+" é "+name.title())

#chamei a função e passei apenas o argumento kind pois o name já tem um valor 
#padrão.
animatizatron2000(kind='cachorro')
