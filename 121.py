#Defini a variável fora do while por que quando ele iniciar ele vai procurar por ela na memória, caso ele não encontre isso retornará um erro.
acao = 'vazia'

#O while será executado enquanto o valor dar var acao for diferente de 'sair'
while acao != 'sair':
    
    #Armazena o que o usuário digitar dentro da var acao
    acao = input('Dgigite  um verbo. (para sair digite "sair")')

    #imprime o conteudo da variável concatenada a uma string
    print(acao+'ando')
#Sim do looop
