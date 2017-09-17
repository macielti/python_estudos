#tentamos dividir 5 por zero
try:
    print(5/0)

#se a divisão der um erro zerodivisionerro ele imprime uma mensagem alternativa
#ao erro
except ZeroDivisionError:
    
    print('Você não pode dividir esses números')
