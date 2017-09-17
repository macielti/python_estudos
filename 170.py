#loop infinito
while True:
    #entrada dos dois numeros
    A= input('Digite o dividendo: ')
    B= input('Digite o divisor: ')
    #tentamos imprimir a divisão dos dois numeros
    try:
        print (str(int(A)/int(B)))
    #se ocorrer o erro então imprimimos uma mensagem personalisada
    except ZeroDivisionError:
        print ('Não é permitida a divisão por 0.')
    


