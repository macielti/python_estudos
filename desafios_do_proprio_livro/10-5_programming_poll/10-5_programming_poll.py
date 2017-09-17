filename= 'resons.txt'

while True:
    rasao= input('Por que você gosta de programação? ')
    
    with open(filename, 'a') as rasoes:
        rasoes.write(rasao+'\n')
