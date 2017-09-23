def bisex(ano):

    return 'O ano ' + str(ano) +(' é ' if (ano%400==0 or ano%4==0) and (ano%100 !=0) else ' não é ')+ 'bissexto'

ano = int(input('Digite um ano: '))

print (bisex(ano))
