frutas_de_que_gosto=["Maracujá", "Laranja", "Morango"]
frutas_amigos=frutas_de_que_gosto[:]
frutas_de_que_gosto.append("Uva")
frutas_amigos.append("Melância")
print("Frutas de que gosto:")
for fruit in frutas_de_que_gosto:
    print(fruit)
print("Frutas que meus amigos gostam:")
for friends in frutas_amigos:
    print(friends)