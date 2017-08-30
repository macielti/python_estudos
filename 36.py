List=["cleber", "cleverson", "bleini"] 
for lista in List:
    print("olá", lista+", como vai? ") 
    print ("que bom,", lista.title(), "\n" )
    
    print ("tchau") 
#o erro de lógica ocorre por que o terceiro print está identado
#logo ele será exibida a cada ciclo do for 
######COREÇAO:#####
List=["cleber", "cleverson", "bleini"] 
for lista in List:
    print("olá", lista+", como vai? ") 
    print ("que bom,", lista.title(), "\n" )
print ("tchau") 