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
        print("Marca: %s\nModelo: %s\nAno: %d\
                " %(self.marca.title(), self.modelo.title(),self.ano))
    
    
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
        """Incrementar o valor do odometro"""
        self.odometro += novo_vl
