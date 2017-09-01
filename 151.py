#objeto chamado carro
class Car():


    def __init__(self, marca, modelo, ano):
        """Função consrutora que recebbe alguns parametros sendo o odometro um
        parametro padrao"""
        self.marca= marca
        self.modelo= modelo
        self.ano= ano
        self.odometro= 0

    
    def descricao(self):
        """Função que imprime a descrição do carro"""
        print("Marca: %s\nModelo: %s\nAno: %d" %(self.marca, self.modelo,
        self.ano))
    
    
    def atualizar_odo(self, novo_vl):
        """Esta função ou método atribui um novo valor ao odometro"""
        self.odometro= novo_vl
    
#criada um objeto chamado car com tres atributos
car= Car('tabajara', 'fusca', 1500)

#impressão o valor do odometro
print('Odometro: '+str(car.odometro))

#chamo o metodo criado para atualizar o valor do odometro e uso 23 como arg
car.atualizar_odo(23)

#imprimo o novo valor do odometro
print('Odometro: '+str(car.odometro))
