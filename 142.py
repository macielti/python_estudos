#Funcção para transferir cada ultimo elemento da lista por ciclo de cada vez
def compilator(arg1,arg2):
    while arg1:
        compilling = arg1.pop()
        arg2.append(compilling)

#Função para printar os elementos da lista usando o for 
def show_content(arg_list):
    for element in arg_list:
        print(element)

#Duas listas de entrada
lista_de_codes = ['arduino.py', 'raspberry.py', 'voice.py', 'arch.py']
lista_compilados = []

#Chamo a função entrando com duas listas, a segunda é vazia
compilator(lista_de_codes, lista_compilados)

#Chamo a segunda função que imprime os elementos da lista.
show_content(lista_compilados)


