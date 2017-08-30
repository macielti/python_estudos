#Defini um loop infinito
while True:

    #armazeno o que o usuário digitar dentro de lugar
    lugar = input('\nDigite um lugar onde você gostria de estar:(digite "sair para sair")')

    #Se o valor digitado pelo user for equal a 'sar', entao o loop se end usando o break
    if lugar == 'sair':
        break

    #Mas caso o usuário digite um valor diferente de 'sair', imprimimos o que o user digited concatened with a string,and continue the loop
    else:
        print('Eu também gostaria de estar em '+lugar)
#the end do loop
