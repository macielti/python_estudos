#leio o numero digitado pelo user e armazeno na var num depois de convete-lo para inteiro
num = int(input('Digite um number for saber if he is pear or impar: '))

#usando o if eu verifico se a divisão não tem resto. Se tiver então ele imprime que o número é impar
if num % 2 != 0 :
    print ('o número '+str(num)+' é impar')

# se o número tem resto então ele imprime que o number is par
else:
    print('O número é par.')
