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
        #se o valor atualizado for menor que o valor real do odometro ele recusa
        #o valor e mostra uma mensagem
        if novo_vl < self.odometro:
            print('Voltar o odometro é crime, a policia já foi acionada')
        #Se tudo estiver correto ele atualiza o valor(quando for maior que o
        #real)
        else:
            self.odometro= novo_vl
            

    def imcrementar_odo(self, novo_vl):
        self.odometro += novo_vl
    
#criada um objeto chamado car com tres atributos
car= Car('tabajara', 'fusca', 1500)

#impressão o valor do odometro
print('Odometro: '+str(car.odometro))

#chamo o metodo criado para atualizar o valor do odometro e uso 23 como arg
car.atualizar_odo(23)

#imprimo o novo valor do odometro
print('Odometro: '+str(car.odometro))

#tento atualizar o valor do odometro para um numero menor que o já foi rodado
#mas é retornado uma mensagem de erro programada
car.atualizar_odo(10)

#Imprimo o valor atual
print('Odometro: '+str(car.odometro))

###Novo Carro###
super_maquina= Car('transformers', 'camaro', 2019)

print('----------\n')

#imprimo o valor default de odometro
print(super_maquina.odometro)

#imcremento de valores para o odometro
super_maquina.imcrementar_odo(100)

#imprimo o novo valor do odometro
print(super_maquina.odometro)

#imcremento um novo valor para ter ceteza de que funciona
super_maquina.imcrementar_odo(100)

#imprimo o valor para observar o imcremento
print(super_maquina.odometro)
