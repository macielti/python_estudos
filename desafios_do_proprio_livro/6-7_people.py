#dicionário com algumas informações pessoais
person1={
    'primeiro_nome':'bruno',
    'last_name':'maciel',    
    'age':18,
    'city':'gilbués'
    }

person2={
    'primeiro_nome':'luiz',
    'last_name':'ribeiro',
    'age':19,
    'city':'gilbués'
    }

person3={
    'primeiro_nome':'jefferson',
    'last_name':'souza',
    'age':18,
    'city':'gama'
}

people=[person1, person2, person3]

#Cada print imprime um valor de uma key do dicionario
for pessoa in people:
    for keys, values in pessoa.items():
        print(keys.title()+': '+ str(values).title())
    
    print('\n')
