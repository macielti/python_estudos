class Dogao():
    

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
    def senta(self):
        print(self.nome.title()+' está sentado.')
    

    def peegaa(self):
        print(self.nome.title()+' está por toda a parte.')


    def rola(self):
        print(self.nome.title()+' está rolando.')


dog1= Dogao('milgral', 5)
dog2= Dogao('doge', 7)

dog1.senta()

dog2.senta()

dog1.peegaa()

dog2.peegaa()

dog1.rola()

dog2.rola()
