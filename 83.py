idade=12

if idade < 4:
    preco=0
elif idade < 18:
    preco=5
elif idade < 65:
    preco=10
if idade >= 65:
    preco=5
print("Seu custo de admissão é: "+str(preco))
# com o if, se a idade for menor que 4 o preco é zero.
# com o elif se a idade não for menor que 4 e for menor de 18 pagará 5
#com o elif, se a idade não for menor que 4 e não for menor de 18  e for menor que 65 pagara 10
#a condição do ultimo if é logicamente equivalente ao else que subistituimos.