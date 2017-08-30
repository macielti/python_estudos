onurb={'posição_x':0 ,'posição_y': 25, 'velocidade': 'medio'} #Criação de um diconário com aluns valores
if onurb['velocidade']=='lento':#se o valor de vlocidade for lento, define o valor do incremento para 1
    incremento_x=1
if onurb['velocidade']=='medio':#se o valor de vlocidade for médio, define o valor do incremento para 2
    incremento_x=2
else:                # se o valor de velocidade não for nem lento nem médio, tentão só pode ser rádipo, logo o valor do
#incremento será 3
    incremento_x=3
onurb['posição_x']=onurb['posição_x']+incremento_x # somo o valor do eixo x ao incremento
print("posição inicial= "+str(onurb['posição_x']-incremento_x)) # imprimo a posição inicial
print("posição final= "+str(onurb['posição_x'])) # imprimo a posição final.
