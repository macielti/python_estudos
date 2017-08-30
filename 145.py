#Função que recebe dois argumentos normais, e o terceiro em diante se trasformará em um dicionário
def persona(prim, last, **informs):

	#Dicionario que recebe os dois primeiros argumentos
	pessoa={'prim':prim, 'last':last}
	
	#For que coleta os dados do terceiro argumento em diante para o dicionario de saida
	for chave, valor in informs.items():
		pessoa[chave] = valor
		
	#Retorno o dicionário
	return pessoa

#Chamo e imprimo o resultado da função
print(persona('Bruno', 'Maciel', local='Brasil', trabalho='Segurança da informação'))

  
	

