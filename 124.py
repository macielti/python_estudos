#Definimos o contador que se inicia em 0
count = 0

#Enquanto o contador armazenar um número menor que 10 então ele se repete
while count < 10 :

    #a cada ciclo do loop, adicionamos mais 1 ao contador
    count +=1

    #Se o número for divisível por dois o comando continue deve pular o que vem depois dele retornando ao inicio do loop
    if count % 2 == 0 :
        continue

    #caso o if seja falso o loop imprime o número que não é divisível por two 
    print(count)
