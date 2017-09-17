filename='guest.txt'
nome= input('Digite o seu nome:')

with open(filename, 'w') as guest:
    guest.write(nome)
