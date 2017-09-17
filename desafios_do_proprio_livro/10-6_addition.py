try:
    A= input('Digite o primeiro número: ')
    A= int(A)
    
    B= input('Digite o segundo número: ')
    B= int(B)
except ValueError:
    print('Você não digitou dois números!!!')

else:
    print('Soma '+str(A+B))
