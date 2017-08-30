lista=["carro pica", "celta 2012", "uno" ]
vendedor="paulo guina"
comprador="jailson mendes"	
print(vendedor.title()+": Seja bem vindo.")
print(comprador.title()+": Quantos carros tem na consecionaria?")
print(vendedor.title()+": temos "+str(len(lista))+ " carros.")
print(comprador.title()+ ": quais sao? ")
print(vendedor.title()+": "+lista[0].title()+",",lista[1].title()+",",lista[2].title())
print(comprador.title()+": Eu gostei do", lista[1].title()+". Um",lista[0],"e um",lista[1],"os dois a 80km por hora tu acha que vai ficar um do lado do outro? ")
print(vendedor.title()+": 80km eh 80km arrombado")
print(comprador.title()+": Quanto custa? ")
print(vendedor.title()+": Custa 500 conto.")
print(comprador.title()+": Tá barato. *risos*")
