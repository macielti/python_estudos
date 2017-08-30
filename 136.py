#Essa função recebe duas strings nomes,  e depois concatena eles.
def complet_name(fr,sc):
    complete= fr+' '+sc
    
    #como saida da função temos o nome completo com lestras maiúsculas
    return complete.title()
    
#atribuo o resultado dessa função dentro de mene
mene= complet_name('jailson', 'mendes')

#imprimo o valor de mene
print(mene)
