lista=[valor for valor in range(0,10,2)]
lisatoo=lista[:]
lista.append(80)
lisatoo.append(50)
print(lista)
print(lisatoo)
#isso ocorre por que os elementos foram adicionados apos a cópia assim os elemetos não passaram para a outra lista. Cada lista se tornam individuais.
