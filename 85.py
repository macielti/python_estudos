lista=["Massa","Queijo","Tomate"]
if "Massa" in lista:
    print("Massa adicionada.")
elif "Queijo" in lista:
    print("Queijo adicionado.")
elif "Tomate" in lista:
    print("Tomate adicionado.")
#Se o primeiro if for verdadeiro os elifs não serão. pois para que o elif seja verdadeiro o if anterior deve ser falso
# mesmo que a condição do elif seja verdadeira.