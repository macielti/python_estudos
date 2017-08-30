#Deinimos duas listas, a primeira com os users not confirmeds e a second empyt
not_confirmed = ['jorel', 'borel', 'jamelão', 'galo_cego']
comfirmed = []

#Essa var vai receber os pop pra concatenar na confirmed
verified='nada'

#Temos o contador
count = 0

#Este while executará o número de vezes ugual ao numero de elementos da lista
while not_confirmed:

    #Recortaremos o valor de cada elemento da lista 
    verified = not_confirmed.pop()

    #Printaremos o user que está sendo cortado
    print('\nVerificando user: '+verified.title())

    #Adicionamos o user verificado a lista confirmed
    comfirmed.append(verified)

    #Adicionamos mais um ao contador
    count +=1

#anununciaçao dos users comfirmados
print ('\nUsers Comfirmados:')

#usando o loop for exibimos cada user confirmado
for user in comfirmed:
    print(user.title())
