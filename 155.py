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
        """Incrementar o valor do odometro"""
        self.odometro += novo_vl
    
    
    def show_batterya(self):
        """Mostrar a quantidade de bateria caso o carro seja da classe 
        eletronico"""
        print('Bateria: '+str(self.batterya))
        

#Classe filho da primeira class
class Eletro_Car(Car):
    
    #Construtor da classe que recebe dois orgumentos herdados da primeira class
    # e o terceiro argumento śempre será 2030 visto que os carros eletronicos
    #teoricaente se tornariam populares por volta de 2030(contexto kkk)
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, 2030)
        self.batterya= 70
    
    
        

#nova instancia de carro eletronico        
tesla= Eletro_Car('tesla', 'v_power')

#chamo a descrição do carro tesla
tesla.descricao()

#chamo a quantidade de bateria do tesla
tesla.show_batterya()
