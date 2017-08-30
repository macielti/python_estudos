#Função que recebe o tamanho da pizza e vários sabores
def pizza(tamanho_da_pizza, *coberturas):
	
	#Imprimo o tamnaho a pizza
	print ('Fazendo uma pizza de '+ str(tamanho_da_pizza)+' pedaços e com os seguintes recheios:')
	
	#uso o for para imprimir as cobertuuras como se fosse uma lista
	for cobertura in coberturas:
		print(cobertura.title())

#Chamo a função com tres coberturas
pizza(8, 'queijo', 'tomate', 'peperone')
