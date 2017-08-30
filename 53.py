lista=[valor for valor in range(0,10,2)]
lisatoo=lista
lista.append(80)
lisatoo.append(50)
print(lista)
print(lisatoo)
#isso ocorre por que dessa forma linkamos as duas listas, as duas listas recebem o mesmo valor da alteração mais recente..
