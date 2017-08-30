#Defino uma função que receberá uma lista de nomes como argumento
def sms(persona):

    #O loop for para concatenar a mensagem com o nome da pessoa e imprimir
    for pessoa in lista:
        msm = 'Você é um dos suspeitos, '+pessoa
        print(msm.title())

#Lista que será passada como entrada da função
lista=['bruno', 'manoel', 'joelson']

#Chamo a função com uma lista como argumento
sms(lista)
