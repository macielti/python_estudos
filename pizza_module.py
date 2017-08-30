#Função que recebe o tamanho da pizza e coberturas
def makeador_de_pizza(size, *coberturas):
	
	#Imprimo o tamanho da pizza
	print('Fazendo uma pizza com '+str(size)+' com os seguintes sabores:')
	
	#For para imprimir a lista de coberturas
	for cobertura in coberturas:
		print(cobertura.title())
