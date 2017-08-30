coberturas_disponiveis=["Calabreza", "Atum", "Cebola"]
pedidos=["Cebola","Portuguesa","Calabreza","Alho","Atum"]
for pedido in pedidos:
    if pedido in coberturas_disponiveis:
        print("Adicionanado "+pedido)
    else:
        print("Não temos "+pedido+" no momento.")