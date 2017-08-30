#usando o imput eu lí o valor do teclado e armazenei em alt
alt = input('Qual é a tua altura?(polegadas)')

#condição if para se a altura for maior ou igua a 36
if int(alt) >= 36:
    #imprimo uma string
    print('Altura aprovada.')

#se o if for falso então o else será executado
else:
    print('Não vai dar.')
    print('Que não vai dar o que rapá?\nSaí de casa cedo comi pra caralho!!!')
