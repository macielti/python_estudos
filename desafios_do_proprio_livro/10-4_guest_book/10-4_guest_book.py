filename= 'guest_book.txt'

while True:
    nome= input('Digite o teu nome: ')
    print('Seja bem vindo, '+nome.title())
    
    with open(filename, 'a') as guest_book:
        guest_book.write(nome.title() + ' visitou o programa.\n')
