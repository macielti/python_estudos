#classe chamada dogao
class Dogao():
    
    
    def __init__(self, nome, idade):
        """Função construtora que recebe alguns parâmetros"""    
        self.nome = nome
        self.idade = idade
    
    
    def senta(self):
        """Metodo que imprime uma mensagem"""
        print(self.nome.title()+' está sentado.')
    

    def peegaa(self):
        """Método que iimprime outra mensagem comcatenada com uma instancia"""
        print(self.nome.title()+' está por toda a parte.')


    def rola(self):
        """Outro metodo que imprime mais uma mensagem concatenada com uma
        instancia"""
        print(self.nome.title()+' está rolando.')

#Objeto chamado dog1 e dog2 que recebe dois argumentos
dog1= Dogao('milgral', 5)
dog2= Dogao('doge', 7)

#chamada de alguns métodos para cada objeto
dog1.senta()
dog2.senta()
dog1.peegaa()
dog2.peegaa()
dog1.rola()
dog2.rola()
