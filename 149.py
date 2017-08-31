#classe camada carro
class Car():

    
    def __init__(self, marca, modelo, ano):
        """Função construtora que recebe 3 argumentos"""
        self.marca= marca
        self.modelo= modelo
        self.ano= ano
    
    def descricao(self):
        """Função que imprime uma descrição do objeto carro"""
        print("Marca: %s\nModelo: %s\nAno: %d" %(self.marca, self.modelo,
        self.ano))

#Criação de um objeto chamado car, com alguns parâmetros
car= Car('tabajara', 'fusca', 1500)

#chamada do metodo descrição
car.descricao()
