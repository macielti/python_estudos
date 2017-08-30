idade=12

if idade < 4:
    preco=0
elif idade < 18:
    preco=5
else:
    preco=10
print("Seu custo de admissão é: "+str(preco))
#em cada uma das verificações que forem verdadeiras será atribuido um valor diferente a variável preço;
# a função str serve para converter um valor inteiro para string um vez que o print só funciona com strings.